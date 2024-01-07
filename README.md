# WebSockets
Learning the Websockets in python

---

# WebSocket Chat Application

This project consists of a simple WebSocket server and client implementation in Python. The server can handle multiple client connections and broadcasts messages sent by one client to all other connected clients. The client can send and receive messages concurrently.

## Requirements

- Python 3.7 or higher
- `websockets` library for Python
- `prompt_toolkit` library for Python (for the client)

## Installation

First, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Install the required Python libraries using pip:

```bash
pip install websockets prompt_toolkit
```

## Usage

### Running the Server

To start the WebSocket server, run:

```bash
python server.py
```

The server will start on `localhost` at port `8765`.

### Running the Client

To connect to the WebSocket server as a client, run:

```bash
python client.py client1
python client.py client2

```

You can open multiple terminals and run the client script in each to simulate multiple clients.

### Interacting in the Chat

Once the client is connected, you can type messages and see responses from the server. Messages sent from one client will be broadcast to all other connected clients.

## Files

- `server.py`: Contains the server logic. It listens for incoming WebSocket connections and broadcasts messages to all connected clients.
- `client.py`: Implements the client logic. It connects to the WebSocket server and handles sending and receiving messages concurrently.

## Notes

- This application is a basic example of using WebSockets in Python.
- The client uses `prompt_toolkit` for non-blocking user input to prevent the event loop from being blocked.
- The server and client scripts are designed to be run in a local environment for demonstration purposes.

## License

This project is open source and available under the [MIT License](LICENSE).

---

This README provides a basic overview of the project, including how to install and run the server and client, as well as a brief description of each file. You can expand the README with more details specific to your project as needed. If you have a license file, you can mention it in the License section; otherwise, you can remove or modify that part.
