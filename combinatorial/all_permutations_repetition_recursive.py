"""
Write an algorithms that generates all permutations of strings with repeated chars, like 
'11234' or '11111' or '11211'

Realize that order is not important when character is the same.

ref. https://betterexplained.com/articles/easy-permutations-and-combinations/
"""


# SOLUTION base on algorithm L - Knuth
# Renzo implemented a nice solution based on dictionary comparison - https://github.com/renzon/code_interview_training/blob/0e06e1d872ebc8edf1a2667296f95e15b9172378/perm_with_rep.py#L19-L19

def find_all_permutations_r(prefix, sublist):
    if len(sublist) == 1:
        print ("prefix = {} sublist = {}".format(prefix, sublist))
        yield prefix + sublist
        return
    for pivot in range(len(sublist)):
        print ("prefix = {} sublist = {} pivot = {}".format(prefix, sublist, pivot))
        # Exchange first char by pivot
        if (sublist[0] == sublist[pivot] and pivot != 0) or sublist[0] in prefix:
            print ("continue")
            continue
        temp = sublist[pivot]
        sublist[pivot] = sublist[0]
        sublist[0] = temp
        yield from find_all_permutations_r(prefix + [sublist[0]], sublist[1:])
        # Exchange back
        sublist[0] = sublist[pivot]
        sublist[pivot] = temp


def find_all_permutations(l):
    for perm in find_all_permutations_r(list(), l):
        yield perm


def test_it(input):
    print ("\nInput = {}\n".format(input))
    for i, p in enumerate(find_all_permutations(list(input))):
        print ("p[{}] = {}".format(i+1, p))


test_it("112")
test_it("1112")
test_it("1111")
test_it("1122")
