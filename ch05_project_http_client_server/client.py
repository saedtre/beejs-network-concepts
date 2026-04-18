"""HTTP Client — ch04 Project: HTTP Client and Server"""

import socket
import sys


def send_request(host: str, port: int, path: str = "/") -> str:
    """Open a TCP connection and send a bare HTTP/1.0 GET request.

    Returns the full response as a string.
    """
    raise NotImplementedError


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    print(send_request(host, port))


if __name__ == "__main__":
    main()
