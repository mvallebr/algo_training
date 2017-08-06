# Graph algorithms

# Concepts

* Maximum flow - https://en.m.wikipedia.org/wiki/Maximum_flow_problem
* Minimum cut - https://en.wikipedia.org/wiki/Minimum_cut

# Dijkstra shortest path

See greedy algorithms section, it's there

# Kruskal’s algorithm 

See greedy algorithms section, it's there

# Prim’s algorithm 

See greedy algorithms section, it's there

# Kruskal vs Prim

Sparse graph -> many edges few vertices -> Prim -> O(E + V log V)
Filled graph -> few edges many vertices -> Kruskal -> O(E log V)

Use Prim's algorithm when you have a graph with lots of edges.
For a graph with V vertices E edges, Kruskal's algorithm runs in O(E log V) time and Prim's algorithm can run in O(E + V log V) amortized time, if you use a Fibonacci Heap.
Prim's algorithm is significantly faster in the limit when you've got a really dense graph with many more edges than vertices. Kruskal performs better in typical situations (sparse graphs) because it uses simpler data structures.

https://www.quora.com/What-is-the-difference-in-Kruskals-and-Prims-algorithm

https://stackoverflow.com/questions/1195872/kruskal-vs-prim

