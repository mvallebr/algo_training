#!/usr/bin/env python3
"""
Given a list L and a number X, find whether any subset of L has sum = X
For instance, for L = [-7, -3, -2, 5, 8] and X = 0, the answer is True - [-3, -2, 5]
"""


def subset_sum(l, x):
    """l should be order as input"""
    bottom = min(l)
    top = x

    # stores whether col can be formed with elements of row
    n_rows = len(l)  # Each row is 1 element of input list
    # Each col is a possible sum and stores subproblem for prior elements =l[:row] and x=col number. 0 is a subproblem
    n_cols = top - bottom + 1
    m = [0] * n_rows * n_cols

    def _id(row, col): return row * n_cols + col

    def _get_m(row, col):
        return m[_id(row, col)] if row >= 0 and row < n_rows and col >= 0 and col < n_cols else False

    for row in range(n_rows):
        for col in range(n_cols):
            col_v = col + bottom
            # Can I sum COL with elements l[:row] ?
            if l[row] - col_v == 0:
                m[_id(row, col)] = True
            else:
                m[_id(row, col)] = _get_m(
                    row - 1, col) or _get_m(row - 1, col - l[row])

    # At this point, if a boolean value is enough, we should return _get_m(n_rows - 1, n_cols - 1)

    def print_m():
        for row in range(n_rows):
            print (l[row], ": ", end=" ")
            for col in range(n_cols):
                print (col + bottom, "T" if m[_id(row, col)] else "F", end=" ")
            print ("")
        print ("min = {} max={}".format(bottom, top))
    print_m()

    # Get Resulting set traversing through the memoazing matrix
    result = []
    col = n_cols - 1
    row = n_rows - 1
    while _get_m(row, col):
        while _get_m(row - 1, col):
            row -= 1
        if row < 0:
            break
        result.append(l[row])
        col -= l[row]

    print (result)
    return result


assert set(subset_sum([-7, -3, -2, 8, 12], 0)) == set([-7, -3, -2, 12])
