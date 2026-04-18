"""TCP Checksum Validator — ch15 Project"""

import struct


def ones_complement_sum(data: bytes) -> int:
    """Return the one's-complement sum of all 16-bit words in data.

    Pad with a zero byte if len(data) is odd.
    """
    raise NotImplementedError


def build_pseudo_header(
    src_ip: str, dst_ip: str, tcp_length: int
) -> bytes:
    """Build the 12-byte IPv4 TCP pseudo-header.

    Layout: src_addr(4) | dst_addr(4) | zero(1) | protocol=6(1) | tcp_length(2)
    """
    raise NotImplementedError


def validate_tcp_checksum(
    src_ip: str, dst_ip: str, tcp_segment: bytes
) -> bool:
    """Return True if the TCP checksum in tcp_segment is valid."""
    raise NotImplementedError


if __name__ == "__main__":
    # Example — fill in with a real captured packet to test
    src = "192.168.1.1"
    dst = "192.168.1.2"
    # raw TCP segment bytes (header + data) with correct checksum:
    segment = bytes(20)  # replace with real data
    print(f"Valid: {validate_tcp_checksum(src, dst, segment)}")
