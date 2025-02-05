# UDP File Transfer System

This project implements a UDP-based file transfer system, allowing a client to request and receive files from a server. The system includes error handling and packet loss simulation to mimic real-world network conditions.

## Features
- **UDP Protocol**: Utilizes UDP for fast file transfer.
- **Packet Loss Simulation**: Simulates real-world network conditions with configurable packet loss.
- **File Transfer**: Supports transferring small, medium, and large files.
- **ACK Mechanism**: Implements an acknowledgment system to ensure reliable delivery.

## Files
- `client.py`: The client-side script that requests and receives files from the server.
- `server.py`: The server-side script that sends files to the client.
- `test.py`: A test script to verify packet creation and handling.
- `run.txt`: Instructions on how to run the client and server.

## How to Use
1. **Run the Server**:
   ```bash
   python server.py "127.1" 15000
2. **Run the Client**:
   ```bash
   python client.py SmallFile.png
   
- Replace SmallFile.png with MediumFile.jpg or LargFile.jpg for different files.

3. **Test Packet Handling**:
   ```bash
   python test.py
   
## Requirements
 **Python 3.x**

