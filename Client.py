# client.py
import asyncio
import websockets
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

async def listen(websocket):
    try:
        while True:
            message = await websocket.recv()
            print(f"\nReceived from server: {message}")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"\nConnection closed: {e}")
    except Exception as e:
        print(f"\nError in listen: {e}")

async def send(websocket, session):
    try:
        while True:
            with patch_stdout():
                message = await session.prompt_async("Enter a message: ")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"\nConnection closed: {e}")
    except Exception as e:
        print(f"\nError in send: {e}")

async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        session = PromptSession()
        listen_task = asyncio.create_task(listen(websocket))
        send_task = asyncio.create_task(send(websocket, session))
        await asyncio.gather(listen_task, send_task)

if __name__ == "__main__":
    asyncio.run(main())
