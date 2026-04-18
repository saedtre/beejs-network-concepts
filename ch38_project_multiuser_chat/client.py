"""Multiuser Chat Client — ch38 Project"""

import json
import select
import socket
import sys


def send_json(conn: socket.socket, obj: dict) -> None:
    """Send obj as a newline-terminated JSON line."""
    raise NotImplementedError


def recv_line(conn: socket.socket) -> str | None:
    """Read one newline-terminated line from conn. Returns None on disconnect."""
    raise NotImplementedError


def run_client(host: str, port: int, nick: str) -> None:
    """Connect, send hello, then multiplex stdin and socket with select.select()."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <host> <port> <nick>")
        sys.exit(1)

    host, port, nick = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    run_client(host, port, nick)


if __name__ == "__main__":
    main()
