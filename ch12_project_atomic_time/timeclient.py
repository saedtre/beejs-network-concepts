"""Atomic Time Client — ch11 Project"""

import socket
import time
from datetime import datetime


def system_seconds_since_1900():
    """
    The time server returns the number of seconds isnce 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch


def fetch_time(host: str, port: int = 37) -> int:
    """Connect to host:port, read 4 bytes, return the 32-bit timestamp."""
    s = socket.socket()
    full_address = (host, port)
    s.connect(full_address)

    buffer = b""
    while True:
        chunk = s.recv(4096)
        if len(chunk) == 0:
            break
        buffer += chunk

    time_bytes = buffer[:4]
    return time_bytes


def decode_timestamp(raw: bytes) -> datetime:
    """Convert an RFC 868 32-bit second count to a UTC datetime."""
    num = int.from_bytes(raw, "big")
    return datetime.fromtimestamp(num)


def main():
    host = "time.nist.gov"
    raw = fetch_time(host)
    dt = decode_timestamp(raw)
    print(f"System time: {dt.isoformat()}")


if __name__ == "__main__":
    main()
