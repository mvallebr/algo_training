"""
Given an integer X and a list L, find the first pair in L whose sum is X
"""


def find_pair_with_sum(X, l):
    """
    Returns True if there is a sum, False if there isn't
    """
    complement = set()
    for i in range(len(l)):
        if l[i] in complement:
            return True
        complement.add(X - l[i])
    return None


l = [3, 34, 4, 12, 5, 2]
X = 5
print ("In the list {} sum {} {}".format(
    l, X, "exists" if find_pair_with_sum(X, l) else "doesn't exist"))


l = [-16, 50, 17, 33, 51, 0]
X = 50
print ("In the list {} sum {} {}".format(
    l, X, "exists" if find_pair_with_sum(X, l) else "doesn't exist"))

l = [-16, 66, 50, 17, 33, 51, 0]
X = 50
print ("In the list {} sum {} {}".format(
    l, X, "exists" if find_pair_with_sum(X, l) else "doesn't exist"))

l = [-167, 66, 50, 17, 34, 51, 10]
X = 50
print ("In the list {} sum {} {}".format(
    l, X, "exists" if find_pair_with_sum(X, l) else "doesn't exist"))
