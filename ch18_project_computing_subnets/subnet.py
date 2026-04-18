"""Subnet Calculator — ch18 Project"""

import sys


def ip_to_int(ip: str) -> int:
    """Convert dotted-decimal IPv4 string to a 32-bit integer."""
    raise NotImplementedError


def int_to_ip(n: int) -> str:
    """Convert a 32-bit integer to dotted-decimal IPv4 string."""
    raise NotImplementedError


def network_address(ip: str, prefix_len: int) -> str:
    """Return the network address for the given IP and prefix length."""
    raise NotImplementedError


def broadcast_address(ip: str, prefix_len: int) -> str:
    """Return the broadcast address for the given IP and prefix length."""
    raise NotImplementedError


def same_subnet(ip1: str, ip2: str, prefix_len: int) -> bool:
    """Return True if ip1 and ip2 are on the same /<prefix_len> subnet."""
    raise NotImplementedError


def host_addresses(ip: str, prefix_len: int) -> list[str]:
    """Return all usable host addresses in the subnet (excludes network/broadcast)."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ip> <prefix_len>")
        sys.exit(1)

    ip, prefix_len = sys.argv[1], int(sys.argv[2])
    print(f"Network:   {network_address(ip, prefix_len)}")
    print(f"Broadcast: {broadcast_address(ip, prefix_len)}")
    print(f"Hosts:     {host_addresses(ip, prefix_len)}")


if __name__ == "__main__":
    main()
