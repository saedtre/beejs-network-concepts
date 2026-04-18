"""HTTP Server — ch04 Project: HTTP Client and Server"""

import socket
import sys


def handle_connection(conn: socket.socket, addr: tuple) -> None:
    """Read an HTTP request from conn and send a minimal response."""
    raise NotImplementedError


def run_server(port: int) -> None:
    """Listen on the given port and handle one connection at a time."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)

    run_server(int(sys.argv[1]))


if __name__ == "__main__":
    main()
