# Project: Port Scanning

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Build a TCP port scanner that attempts to connect to each port in a range
and reports whether the port is open or closed.

**Only scan hosts you own or have explicit permission to scan.**

## Run
```bash
python scanner.py localhost 1 1024
```
Expected output: one line per open port found.
