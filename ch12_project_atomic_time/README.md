# Project: Atomic Time

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Connect to a NIST time server on port 37 (RFC 868 Time Protocol), receive a
32-bit big-endian timestamp (seconds since 1900-01-01), and convert it to a
human-readable UTC datetime.

## Run
```bash
python atomic_time.py time.nist.gov
```
