"""
Write an algorithms that generates all permutations of the string 
'abcdefghklmnopqrstuvwxyz0123456789'

As it's permutation, order is important.

ref. https://brilliant.org/wiki/permutations-with-repetition/
"""



def all_perms(a, ini):
  if ini == len(a):
    yield a[:]
  for i in range(ini, len(a)):
    a[ini], a[i] = a[i], a[ini]
    yield from all_perms(a, ini+1)     
    a[ini], a[i] = a[i], a[ini]
    
l = list(all_perms(list("abc"), 0))
print (str(l), len(l))