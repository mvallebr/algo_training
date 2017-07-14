#!/usr/bin/env python
"""
Given a list L and a number X, find whether any subset of L has sum = X
For instance, for L = [-7, -3, -2, 5, 8] and X = 0, the answer is True - [-3, -2, 5]
"""


def subset_sum(l, x):
    """l should be order as input"""
    bottom = min(l)
    top = max(l)

    def _id(row, col): return row * (top - bottom) + col

    # stores whether col can be formed with elements of row
    m = [0] * len(l) * (top - bottom)
    for row in range(len(l)):  # row goes through all possible values until the maximum sum
        for col in range(top - bottom):  # col goes through elements of the list
            if col == 0:
                m[_id(row, col)] = True
            elif l[row] - bottom == col:  # translades l[row] to have bottom as reference
                m[_id(row, col)] = True
            else:
                id_previous_row = _id(row - 1, col)
                id_previous_row_minus_col = _id(row - 1, col - (l[row] - bottom))
                if id_previous_row > 0 and m[id_previous_row]:
                    m[_id(row, col)] = m[id_previous_row]
                if id_previous_row_minus_col > 0 and m[id_previous_row_minus_col]:
                    m[_id(row, col)] = m[id_previous_row_minus_col]
                else:
                    m[_id(row, col)] = False
    for row in range(len(l)):
        print l[row], ": ", 
        for col in range(top - bottom):
            print m[_id(row, col)],
        print ("")
    print ("min = {} max={}".format(bottom, top))
    result = []
    col = top - bottom - 1
    row = len(l) - 1
    while m[_id(row, col)]:
        print "b", row+1, col+1
        while row > 0 and m[_id(row - 1, col)]:
            row -= 1
        print row+1, col+1
        if row < 0:
            break
        result.append(l[row])
        col -= row
        if  col < 0:
            break

    return result


print (subset_sum([-7, -3, -2, 5, 8], 0))
assert set(subset_sum([-7, -3, -2, 5, 8], 0)) == set([-3, -2, 5])
