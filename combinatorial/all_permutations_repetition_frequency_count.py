"""
Write an algorithms that generates all permutations of strings with repeated chars, like
'11234' or '11111' or '11211'

Realize that order is not important when character is the same.

ref. https://betterexplained.com/articles/easy-permutations-and-combinations/
"""

# Renzo implemented a nice solution based on frequency mapping - https://github.com/renzon/code_interview_training/blob/0e06e1d872ebc8edf1a2667296f95e15b9172378/perm_with_rep.py#L19-L19
# This is my version of the same solution

from collections import Counter

def all_perms_r(curr, unique, freqs):
    if len([v for v in freqs.values() if v > 0]) == 0:
        yield curr[:]
    for i in range(len(unique)):
        if freqs[unique[i]] == 0:
            continue
        ch = unique[i]
        freqs[unique[i]] -= 1
        yield from all_perms_r(curr + ch, unique, freqs)
        freqs[unique[i]] += 1

def all_perms(a):
    yield from all_perms_r("", sorted(Counter(a).keys()), Counter(a))

l = list(all_perms(list("aac")))
print("aac", str(l), len(l))

l = list(all_perms(list("aabc")))
print("aabc", str(l), len(l))