# Project: The Word Server

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Build a client/server pair that exchanges words using length-prefix framing:
each message is sent as a 2-byte big-endian length followed by the UTF-8 word.

### Server
- Listen on a port
- For each connection, send a list of words using the length-prefix protocol

### Client
- Connect to the server
- Receive and print each word

## Packet format
```
[2-byte big-endian length][UTF-8 payload]
```

## Run
```bash
# Terminal 1
python server.py 9000

# Terminal 2
python client.py localhost 9000
```
