# Project: Using Select

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Build a single-threaded server that handles multiple client connections
simultaneously using `select.select()` — no threads, no forking.

## Run
```bash
# Terminal 1
python server.py 9000

# Terminals 2, 3, 4 (multiple clients simultaneously)
nc localhost 9000
```
