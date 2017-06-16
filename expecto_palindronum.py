"""
# Expecto Palindronum
Memory Limit:64 MB
Time Limit: 5 s
A palindrome is a word that reads the same backward and forward. 
Given a string S, you are allowed to convert it to a palindrome by adding 0 or more characters in front of it. 
Find the length of the shortest palindrome that you can create from S by applying the above transformation. 
## Input Specifications
Your program will take
A string S ( 1 ≤ Length(S) ≤ 100) where each character of S will be
a lowercase alphabet (Between 'a' to 'z')
## Output Specifications
For each input, print out an integer L denoting the length of the shortest palindrome you can 
generate from S.
## Sample Input/Output
INPUT
baaa
OUTPUT
7
EXPLANATION
The shortest palindrome you can construct from 'baaa' is 'aaabaaa'.
"""

def find_shortest_palindrome(original):
    s = ""
    t = ""
    start = 0

    for end in range(len(original)-1, 0, -1):
        if start >= end:
            break
        if original[start] == original[end]:
            t += original[start]
            start += 1
        else:
            s += t + original[end]
            start = 0
            t = ""

    return s + original




print (find_shortest_palindrome("abc"))
print (find_shortest_palindrome("aabc"))
print (find_shortest_palindrome("aaaaabc"))
print (find_shortest_palindrome("aaabaaaa"))