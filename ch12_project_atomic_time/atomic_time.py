"""Atomic Time Client — ch11 Project"""

import socket
import sys
from datetime import datetime, timezone


# RFC 868: seconds from 1900-01-01 00:00:00 UTC
EPOCH_1900 = datetime(1900, 1, 1, tzinfo=timezone.utc)


def fetch_time(host: str, port: int = 37) -> int:
    """Connect to host:port, read 4 bytes, return the 32-bit timestamp."""
    raise NotImplementedError


def decode_timestamp(raw: int) -> datetime:
    """Convert an RFC 868 32-bit second count to a UTC datetime."""
    raise NotImplementedError


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <host>")
        sys.exit(1)

    host = sys.argv[1]
    raw = fetch_time(host)
    dt = decode_timestamp(raw)
    print(f"Current time: {dt.isoformat()}")


if __name__ == "__main__":
    main()
