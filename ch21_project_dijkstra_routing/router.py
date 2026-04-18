"""Dijkstra's Routing — ch21 Project"""

import sys
from collections import defaultdict


Graph = dict[str, list[tuple[str, int]]]  # node -> [(neighbour, cost)]


def parse_graph(text: str) -> Graph:
    """Parse adjacency-list text into an undirected weighted graph."""
    raise NotImplementedError


def dijkstra(graph: Graph, source: str) -> dict[str, tuple[int, list[str]]]:
    """Return {node: (total_cost, [path])} for all reachable nodes from source."""
    raise NotImplementedError


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <network_file> <source_node>")
        sys.exit(1)

    path, source = sys.argv[1], sys.argv[2]
    text = open(path).read()
    graph = parse_graph(text)
    results = dijkstra(graph, source)

    for node, (cost, route) in sorted(results.items()):
        print(f"{source} -> {node}: cost={cost}  path={' -> '.join(route)}")


if __name__ == "__main__":
    main()
