"""TCP Port Scanner — ch37 Project"""

import socket
import sys


TIMEOUT = 0.5  # seconds per connection attempt


def scan_port(host: str, port: int) -> bool:
    """Return True if the TCP port is open on host."""
    raise NotImplementedError


def scan_range(host: str, start: int, end: int) -> list[int]:
    """Scan ports start..end (inclusive) and return a list of open ports."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <host> <start_port> <end_port>")
        sys.exit(1)

    host = sys.argv[1]
    start, end = int(sys.argv[2]), int(sys.argv[3])
    open_ports = scan_range(host, start, end)

    if open_ports:
        for p in open_ports:
            print(f"  {p}/tcp  open")
    else:
        print("No open ports found.")


if __name__ == "__main__":
    main()
