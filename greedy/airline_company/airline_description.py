"""
A new airline company is setting up operations and needs your help! They want to optimize their routes so as to cover a full list of cities, wile minimizing the cost of their operations. 
You are provided with the number of N cities and with the costs of operating flights between some of the cities. 
Can you design an algorithm that will return the list of routes that cover all the N cities at the minimum operational cost? 

Assumtions: 
1. not all direct routes between cities are possible, but all cities can be reached either directly of via intermediate cities. You are provided with the complete set of routes that are possible as input to your algorithm. 
2. the costs of operating a route from any city to any other directly connected city is known and unique (i.e., no two costs between direct routes are the same) 
3. the cost of operating a route from city X to city Y is equal to the cost of operating the route from city Y to city X 

Your algorithm will get as input from stdin the following: 
1. on the first line, the number of cities N 
2. on the second line, the total number of possible routes K 
3. on the subsequent K lines, the possible routes between cities and their operational cost, separated by spaces. Cities are integer numbers from 0 to N-1. costs are floats. 

The output of your algorithm should be the list of routes chosen to be operated at the minimum cost, one route per line. After the list of routes, on the final line the total cost of operating all chosen routes should be printed. 

What is the time complexity of the algorithm you've created? 

Example: 
Input 
8 
16 
4 5 0.35 
4 7 0.37 
5 7 0.28 
0 7 0.16 
1 5 0.32 
0 4 0.38 
2 3 0.17 
1 7 0.19 
0 2 0.26 
1 2 0.36 
1 3 0.29 
2 7 0.34 
6 2 0.40 
3 6 0.52 
6 0 0.58 
6 4 0.93 

Output 
0 7 0.16 
2 3 0.17 
1 7 0.19 
0 2 0.26 
5 7 0.28 
4 5 0.35 
6 2 0.40 
1.81

"""