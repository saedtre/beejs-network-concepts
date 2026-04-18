# Project: Validating a TCP Packet

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Given a raw TCP segment (as bytes), compute the TCP checksum using the
pseudo-header (source IP, dest IP, protocol, TCP length) and verify it
matches the checksum field in the segment.

## Algorithm
1. Build the 12-byte IPv4 pseudo-header.
2. Zero out the 2-byte checksum field in the TCP header.
3. Concatenate pseudo-header + TCP segment (header + data).
4. Compute the one's-complement checksum over all 16-bit words.
5. The result should be `0xFFFF` (or `0x0000` after final complement).

## Run
```bash
python checksum.py
```
