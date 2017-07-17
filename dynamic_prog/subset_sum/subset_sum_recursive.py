#!/usr/bin/env python3
"""
Given a list L and a number X, find whether any subset of L has sum = X
For instance, for L = [-7, -3, -2, 5, 8] and X = 0, the answer is True - [-3, -2, 5]
"""


def subset_sum_r(current, l, x):
    for e in l:
        current.append(e)
        if x - e == 0:
            yield current[:]
            return
        l.remove(e)
        yield from subset_sum_r(current, l, x - e)
        l.append(e)
        current.remove(e)


def subset_sum(l, x):
    """l should be ordered on input"""
    yield from subset_sum_r([], l, x)


print (list(subset_sum([-7, -3, -2, 5, 8], 0)))
s1 = set(next(subset_sum([-7, -3, -2, 5, 8], 0)))
s2 = set([-3, -2, 5])
assert len(s1.difference(s2)) == 0 and len(s2.difference(s1)) == 0
