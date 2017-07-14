"""
Given an integer X and a list L, find the first pair in L whose sum is X
"""

def find_pair_with_sum(X, l):
    """
    Returns a tuple with indexes of both elements or None if there is no pair
    """
    complement = set()
    for i in range(len(l)):
        if l[i] in complement:
            return (X -l[i], l[i])
        complement.add(X - l[i])
    return None

l = [3, 34, 4, 12, 5, 2]
X = 5
print ("In the list {} items {} sum {}".format(l, find_pair_with_sum(X,l), X))


l = [-16, 50, 17, 33, 51, 0]
X = 50
print ("In the list {} items {} sum {}".format(l, find_pair_with_sum(X,l), X))


l = [-16, 66, 50, 17, 33, 51, 0]
X = 50
print ("In the list {} items {} sum {}".format(l, find_pair_with_sum(X,l), X))