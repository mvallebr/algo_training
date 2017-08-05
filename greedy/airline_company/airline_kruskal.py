"""
Implementation usng Kruskal algorithm - Minimum Spanning Tree
"""


def read_input(file_name):
    with open("input.txt") as f:
        lines = f.readlines()
    



graph = read_input("input.txt")

print ("graph = {}".format(graph))