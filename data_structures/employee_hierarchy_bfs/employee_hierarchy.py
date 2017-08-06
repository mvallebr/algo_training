#!/usr/bin/env python3

from collections import defaultdict
import os
import re


def read_input(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        lines = f.readlines()
    # num_employees = int(lines[0])
    # Example "Jon Mark"
    pattern = re.compile("(?P<manager>\w+)\s+(?P<employee>\w+)")

    managers = set()
    managed = set()
    relations = defaultdict(set)
    for i in range(1, len(lines)):
        match = pattern.match(lines[i])
        manager = match.group("manager")
        employee = match.group("employee")
        managers.add(manager)
        managed.add(employee)
        relations[manager].add(employee)

    return managers, managed, relations


def main():
    managers, managed, relations = read_input("input1.txt")
    ceos = managers - managed
    level = ceos
    print (" ".join(level))
    while len(level) > 0:
        sublevel = set()
        for person in level:
            sublevel |= relations[person]
        print (" ".join(sublevel))
        level = sublevel


if __name__ == "__main__":
    main()
