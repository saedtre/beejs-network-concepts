"""Multiuser Chat Server — ch38 Project"""

import json
import select
import socket
import sys


def broadcast(message: dict, sender: socket.socket, clients: dict[socket.socket, str]) -> None:
    """Send a JSON message to all clients except sender.

    clients maps socket -> nickname.
    """
    raise NotImplementedError


def handle_message(
    raw: str,
    conn: socket.socket,
    clients: dict[socket.socket, str],
) -> None:
    """Parse a JSON line from conn and act on it (hello or chat)."""
    raise NotImplementedError


def run_server(port: int) -> None:
    """Accept clients and multiplex I/O with select.select()."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    run_server(int(sys.argv[1]))


if __name__ == "__main__":
    main()
