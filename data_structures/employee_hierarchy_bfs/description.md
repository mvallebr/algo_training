# Employee hierarchy problem

Found at: https://www.careercup.com/page?pid=skyscanner-interview-questions

You are given as input on stdin the number of employees in a company and their direct line management relations between each other. Each person in the company can directly line-manage maximum 2 other employees. The input from stdin has the following format: 
1. on the first line, the number of employees 
2. on the subsequent lines, the line management relations in the format «EmployeeM EmployeeN» - meaning EmployeeM manages EmployeeN (names are without spaces and spaces are used to separate the two names). 
The input is correct (there are only direct management relations, no cycles). 
For simplicity, the first line after the number of employees always contains the manager at the top of the hierarchy. 
Write a program that reads the input file and then prints out the employees per level, in order of their importance (i.e. hierarchy): 

Example: 

Input: 
6 
Jon Mark 
Jon David 
Mark Paul 
Paul Lee 
Paul Steve 

Output: 
Jon 
Mark David 
Paul 
Lee Steve 

Input: 
7 
Jon Lee 
Lee Paul 
Paul Mark 
Paul David 
Lee Steve 
Steve Mat 

Output: 
Jon 
Lee 
Paul Steve 
Mark David Mat

