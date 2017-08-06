#!/usr/bin/env python3
"""
Implementation usng Kruskal algorithm - Minimum Spanning Tree
"""

from collections import defaultdict
import os
import re


class KruskalGraph():
    def __init__(self):
        self.nodes = set()
        self.parent_nodes = dict()
        self.ranks = defaultdict(int)  # Disjoint set optimization
        # key = weight, value = list of tuples (node1, node2)
        self.edges = defaultdict(list)

    def find_root(self, node):
        return node if self.parent_nodes[node] == node else self.find_root(self.parent_nodes[node])

    def are_nodes_connected(self, node1, node2):
        return node1 in self.parent_nodes and node2 in self.parent_nodes and self.find_root(node1) == self.find_root(node2)

    def connect_nodes(self, node1, node2):
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if self.ranks[root1] < self.ranks[root2]:
            self.parent_nodes[root1] = root2
        else:
            self.parent_nodes[root2] = root1
            if self.ranks[root2] == self.ranks[root1]:
                self.ranks[root1] += 1

    def add_edge(self, node1, node2, weight):
        self.nodes.add(node1)
        self.nodes.add(node2)
        self.edges[weight].append((node1, node2))
        if node1 not in self.parent_nodes:
            self.parent_nodes[node1] = node1
        if node2 not in self.parent_nodes:
            self.parent_nodes[node2] = node2
        self.connect_nodes(node1, node2)

    def iterate_sorted_edges(self):
        for edge in sorted(self.edges.keys()):
            yield edge, self.edges[edge]

    def __str__(self):
        l = []
        for edge, nodes_list in self.iterate_sorted_edges():
            for node1, node2 in nodes_list:
                l.append("{} {} {}".format(node1, node2, edge))
        return "\n".join(l)

    def sum_of_weights(self):
        return sum(self.edges.keys())


def read_input(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        lines = f.readlines()
    num_cities = int(lines[0])
    num_routes = int(lines[1])
    # Example "4 5 0.35"
    pattern = re.compile(
        "(?P<city1>\d)\s+(?P<city2>\d)\s+(?P<cost>\d.+\.?\d.*)")
    result = KruskalGraph()
    for i in range(2, len(lines)):
        match = pattern.match(lines[i])
        city1 = match.group("city1")
        city2 = match.group("city2")
        cost = float(match.group("cost"))
        result.add_edge(city1, city2, cost)
    return result


def main():
    graph = read_input("input.txt")

    print ("input:")
    print (graph)

    result = KruskalGraph()
    for weight, cities_list in graph.iterate_sorted_edges():
        for city1, city2 in cities_list:
            if not result.are_nodes_connected(city1, city2):
                result.add_edge(city1, city2, weight)

    if len(result.nodes) != len(graph.nodes):
        raise Exception("Couldn't find a minimum spanning tree")

    print ("output")
    print (result)
    print (result.sum_of_weights())


if __name__ == "__main__":
    main()
