"""Better Web Server — ch08 Project"""

import socket
import sys
from pathlib import Path


def read_file(root: Path, request_path: str) -> bytes | None:
    """Return file bytes for request_path under root, or None if not found."""
    raise NotImplementedError


def make_response(status_code: int, body: bytes, content_type: str = "text/html") -> bytes:
    """Build a minimal HTTP/1.0 response."""
    raise NotImplementedError


def handle_connection(conn: socket.socket, addr: tuple, root: Path) -> None:
    """Parse the request, read the file, send the response."""
    raise NotImplementedError


def run_server(root: Path, port: int) -> None:
    """Listen on port and serve files from root."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <webroot> <port>")
        sys.exit(1)

    root = Path(sys.argv[1])
    port = int(sys.argv[2])
    run_server(root, port)


if __name__ == "__main__":
    main()
