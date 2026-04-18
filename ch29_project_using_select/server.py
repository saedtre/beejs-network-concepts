"""Multiplexed Server with select() — ch29 Project"""

import select
import socket
import sys


def run_server(port: int) -> None:
    """Accept and handle multiple clients concurrently using select.select().

    For each incoming message, echo it back to the sender and broadcast
    it to all other connected clients.
    """
    raise NotImplementedError


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    run_server(int(sys.argv[1]))


if __name__ == "__main__":
    main()
