"""
Write an algorithms that generates all permutations of the string 
'abcdefghklmnopqrstuvwxyz0123456789'

As it's permutation, order is important.

ref. https://brilliant.org/wiki/permutations-with-repetition/
"""


def find_all_permutations_r(prefix, sublist):
    if len(sublist) == 1:
        yield prefix + sublist
    for pivot in range(len(sublist)):
        # Exchange first char by pivot
        sublist[0], sublist[pivot] = sublist[pivot], sublist[0] 
        yield from find_all_permutations_r(prefix + [sublist[0]], sublist[1:])
        # Exchange back
        sublist[0], sublist[pivot] = sublist[pivot], sublist[0] 


def find_all_permutations(l):
    for perm in find_all_permutations_r(list(), l):
        yield perm


def count_num_perms(input):
    c = 0
    for x in find_all_permutations(input[:]):
        c += 1
    print("Found {} permutations".format(c))


def print_all_perms(input):
    print("\nPrinting all permutations for {}".format(input))
    for i, x in enumerate(find_all_permutations(input[:])):
        print ("perm[{}] = {}".format(i + 1, "".join(x)))


print_all_perms(list("123"))
print_all_perms(list("12345"))
# count_num_perms(list('abcdefghklmnopqrstuvwxyz0123456789'))
