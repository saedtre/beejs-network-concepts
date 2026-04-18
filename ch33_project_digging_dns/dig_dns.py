"""DNS Dig — ch33 Project"""

import socket
import sys


def lookup_a(hostname: str) -> list[str]:
    """Return all IPv4 addresses for hostname."""
    raise NotImplementedError


def lookup_aaaa(hostname: str) -> list[str]:
    """Return all IPv6 addresses for hostname."""
    raise NotImplementedError


def reverse_lookup(ip: str) -> str:
    """Return the PTR (reverse DNS) record for ip."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    print(f"A records:    {lookup_a(hostname)}")
    print(f"AAAA records: {lookup_aaaa(hostname)}")


if __name__ == "__main__":
    main()
