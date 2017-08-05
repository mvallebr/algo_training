#!/usr/bin/env python3
"""
Implementation usng Kruskal algorithm - Minimum Spanning Tree
"""

from collections import defaultdict
import os
import re


class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_edge(self, node1, node2, weight):
        self.nodes.add(node1)
        self.nodes.add(node2)
        self.edges[weight].append((node1, node2))

    def iterate_sorted_edges(self):
        for edge in sorted(self.edges.keys()):
            yield edge, self.edges[edge]

    def __str__(self):
        l = []
        for edge, nodes_list in self.iterate_sorted_edges():
            for node1, node2 in nodes_list:
                l.append("{} {} {}".format(node1, node2, edge))
        return "\n".join(l)


def read_input(file_name):
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        lines = f.readlines()
    num_cities = int(lines[0])
    num_routes = int(lines[1])
    # Example "4 5 0.35 ""
    pattern = re.compile("(?P<city1>\d)\s.*(?P<city2>\d)\s.*(?P<cost>\d\.\d)")
    result = Graph()
    for i in range(2, num_routes):
        match = pattern.match(lines[i])
        city1 = match.group("city1")
        city2 = match.group("city2")
        cost = float(match.group("cost"))
        result.add_edge(city1, city2, cost)
    return result


def main():
    graph = read_input("input.txt")

    print ("graph:")
    print (graph)

    result = Graph()
    for weight, cities_list in graph.iterate_sorted_edges():
        for city1, city2 in cities_list:
            print(result.nodes)
            # The check here is wrong, what I need to check is whether the 2 subtrees are already connected or not
            if city1 not in result.nodes or city2 not in result.nodes: 
                result.add_edge(city1, city2, weight)

    print ("output")
    print (result)


if __name__ == "__main__":
    main()
