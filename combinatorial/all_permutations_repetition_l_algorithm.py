"""
Write an algorithms that generates all permutations of strings with repeated chars, like
'11234' or '11111' or '11211'

Realize that order is not important when character is the same.

ref. https://betterexplained.com/articles/easy-permutations-and-combinations/
"""

# SOLUTION base on algorithm L - Knuth
# http://blog.bjrn.se/2008/04/lexicographic-permutations-using.html

from collections import Counter


def reverse(seq, start, end):
    while start < end:
        seq[start], seq[end] = seq[end], seq[start]
        start += 1
        end -= 1


def all_perms_r(seq):
    end = len(seq) - 1
    j = end
    if end < 0:  # Empty sequence
        return
    yield seq[:]
    if end < 1:  # sequence of 1 element
        return
    while True:
        j = end - 1
        # Find first sequence of 2 elements when first < second
        while j >= 0 and not seq[j] < seq[j + 1]:
            j -= 1
        if j < 0:
            # We reached last element, (e.g.: 4321)
            break
        # Find first element m > j, after j. Element will be after j because j+1 is greater for sure
        m = end
        while not seq[m] > seq[j]:
            m -= 1
        # For instance 31542 -> j points to 1, m points to 5
        # 31542 becomes 35142
        seq[j], seq[m] = seq[m], seq[j]
        # 35142 becomes 32415, which is next of 31542 lexicografically
        reverse(seq, j + 1, end)
        yield seq[:]


def all_perms(seq):
    yield from all_perms_r(seq)

l = list(all_perms(list("112")))
print("112", str(l), len(l))

l = list(all_perms(list("1123")))
print("1123", str(l), len(l))
