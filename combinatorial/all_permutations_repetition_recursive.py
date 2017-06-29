"""
Write an algorithms that generates all permutations of strings with repeated chars, like 
'11234' or '11111' or '11211'

Realize that order is not important when character is the same.

ref. https://betterexplained.com/articles/easy-permutations-and-combinations/
"""


def find_all_permutations_r(prefix, sublist):
    if len(sublist) == 1:
        yield prefix + sublist
    for pivot in range(len(sublist)):
        print ("pivot = {} {} {}".format(pivot, sublist[pivot], sublist[0]))
        # Exchange first char by pivot
        if sublist[pivot] == sublist[0]:
            yield prefix + sublist
            continue
        temp = sublist[pivot]
        sublist[pivot] = sublist[0]
        sublist[0] = temp
        for perm in find_all_permutations_r(prefix + [sublist[0]], sublist[1:]):
            yield perm
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


test_it("1112")
#test_it("1111")
# test_it("1234")
