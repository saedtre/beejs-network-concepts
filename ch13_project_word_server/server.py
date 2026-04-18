"""Word Server — ch12 Project"""

import socket
import sys


WORDS = ["apple", "banana", "cherry", "date", "elderberry"]


def send_word(conn: socket.socket, word: str) -> None:
    """Send a single word using 2-byte big-endian length-prefix framing."""
    raise NotImplementedError


def handle_connection(conn: socket.socket, addr: tuple) -> None:
    """Send all words to the connected client."""
    raise NotImplementedError


def run_server(port: int) -> None:
    raise NotImplementedError


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        sys.exit(1)
    run_server(int(sys.argv[1]))


if __name__ == "__main__":
    main()
