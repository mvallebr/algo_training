"""
Implementation usng Kruskal algorithm - Minimum Spanning Tree
"""

from collections import defaultdict
import os
import re

class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, node1, node2, weight):
        self.nodes.add(node1)
        self.nodes.add(node2)
        self.edges[weight] = (node1, node2)

    def __str__(self):
        l = []
        for edge, nodes in self.edges:
            l.append("{} {} {}".format(nodes(0), nodes(1), edge))
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



graph = read_input("input.txt")

print ("graph = {}".format(graph))
