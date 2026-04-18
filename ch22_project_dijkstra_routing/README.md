# Project: Routing with Dijkstra's Algorithm

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Model a network as a weighted graph and use Dijkstra's shortest-path
algorithm to compute the routing table for a given source node.

## Input format (adjacency list)
```
A B 1
A C 4
B C 2
B D 5
C D 1
```
Each line: `<node1> <node2> <cost>`

## Run
```bash
python router.py network.txt A
```
Expected output: shortest cost and path from A to every other node.
