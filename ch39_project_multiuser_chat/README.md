# Project: Multiuser Chat Client and Server

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Build a multiuser chat system where the server uses `select()` to handle
many clients simultaneously and messages are exchanged as newline-delimited
JSON packets.

## Protocol
Each message is one JSON object per line (newline-delimited JSON / NDJSON):

```json
{"type": "hello", "nick": "alice"}
{"type": "chat", "message": "hello everyone!"}
{"type": "chat", "nick": "alice", "message": "hello everyone!"}
```

- Client sends `hello` with chosen nickname on connect.
- Client sends `chat` messages.
- Server broadcasts `chat` messages (adding `nick`) to all other clients.

## Run
```bash
# Terminal 1
python server.py 9000

# Terminals 2+
python client.py localhost 9000
```
