# Project: Sniff ARP Packets with WireShark

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Use WireShark to capture and inspect ARP packets on your local network.

## Steps
1. Install WireShark: https://www.wireshark.org/
2. Start a capture on your active network interface.
3. Apply display filter: `arp`
4. Ping a device on your LAN to trigger ARP traffic.
5. Examine the ARP request and reply frames:
   - Sender MAC / Sender IP
   - Target MAC / Target IP
   - Opcode (1 = request, 2 = reply)

## What to look for
- Broadcast destination MAC (`ff:ff:ff:ff:ff:ff`) on requests
- The reply is unicast back to the requester

## Notes
<!-- Record what you observed -->
