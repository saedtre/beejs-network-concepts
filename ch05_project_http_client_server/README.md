# Project: HTTP Client and Server

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Build a minimal HTTP/1.0 client and server using raw sockets.

### Client
- Open a TCP socket to a given host/port
- Send a raw `GET / HTTP/1.0\r\n\r\n` request
- Print the response

### Server
- Listen on a given port
- Accept connections
- Parse the incoming request line
- Return a minimal HTTP response

## Run
```bash
# Terminal 1
python server.py 8080

# Terminal 2
python client.py localhost 8080
```
