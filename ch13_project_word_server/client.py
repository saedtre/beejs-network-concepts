"""Word Client — ch12 Project"""

import socket
import sys


def recv_word(conn: socket.socket) -> str | None:
    """Read one length-prefixed word. Returns None on EOF."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <port>")
        sys.exit(1)

    host, port = sys.argv[1], int(sys.argv[2])
    with socket.create_connection((host, port)) as conn:
        while (word := recv_word(conn)) is not None:
            print(word)


if __name__ == "__main__":
    main()
