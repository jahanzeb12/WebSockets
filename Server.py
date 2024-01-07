import asyncio
import websockets

connected = set()

async def echo(websocket, path):
    # Register websocket connection
    connected.add(websocket)
    print(f"New client connected. Total clients: {len(connected)}")
    try:
        async for message in websocket:
            print(f"Received message: '{message}' from {websocket.remote_address}")
            # Broadcast message to all connected clients except itself
            for conn in connected:
                if conn != websocket:
                    try:
                        await conn.send(f"Echo: {message}")
                        print(f"Sent message to {conn.remote_address}")
                    except Exception as e:
                        print(f"Error sending message to {conn.remote_address}: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Unregister websocket connection
        connected.remove(websocket)
        print(f"Client disconnected. Total clients: {len(connected)}")

start_server = websockets.serve(echo, "localhost", 8765,ping_interval=1000, ping_timeout=1000)

asyncio.get_event_loop().run_until_complete(start_server)
print("Server started...")
asyncio.get_event_loop().run_forever()
