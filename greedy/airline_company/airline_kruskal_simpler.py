#!/usr/bin/env python3
"""
Implementation usng Kruskal algorithm - Minimum Spanning Tree
"""

from collections import defaultdict
import os
import re


def read_input(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        lines = f.readlines()
    num_cities = int(lines[0])
    num_routes = int(lines[1])
    # Example "4 5 0.35"
    pattern = re.compile(
        "(?P<city1>\d)\s+(?P<city2>\d)\s+(?P<cost>\d.+\.?\d.*)")
    result = []
    for i in range(2, len(lines)):
        match = pattern.match(lines[i])
        city1 = match.group("city1")
        city2 = match.group("city2")
        cost = float(match.group("cost"))
        result.append((city1, city2, cost))
    return result


def find_root(node, parent_nodes):
    if node not in parent_nodes or parent_nodes[node] == node:
        return node
    else:
        parent_nodes[node] = find_root(
            parent_nodes[node], parent_nodes)  # path compression
        return parent_nodes[node]


def kruskal_union_find(graph):
    parent_nodes = dict()
    ranks = defaultdict(int)  # Disjoint set optimization

    for node1, node2, weigth in sorted(graph, key=lambda e: e[2]):
        root1 = find_root(node1, parent_nodes)
        root2 = find_root(node2, parent_nodes)
        if root1 != root2:  # Not connected
            if ranks[root1] < ranks[root2]:
                parent_nodes[root1] = root2
            else:
                parent_nodes[root2] = root1
                if ranks[root2] < ranks[root1]:
                    ranks[root1] += 1
            yield node1, node2, weigth

    return []


def main():
    graph = read_input("input.txt")

    print ("input:")
    print (graph)

    total_cost = 0.0
    for city1, city2, cost in kruskal_union_find(graph):
        print("{} {} {}".format(city1, city2, cost))
        total_cost += cost
    print (total_cost)


if __name__ == "__main__":
    main()
