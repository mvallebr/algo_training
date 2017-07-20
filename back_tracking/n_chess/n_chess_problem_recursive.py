"""
Objec­tive : In chess, a queen can move as far as she pleases, hor­i­zon­tally, ver­ti­cally, or diag­o­nally. A chess board has 8 rows and 8 columns. The stan­dard 8 by 8 Queen’s prob­lem asks how to place 8 queens on an ordi­nary chess board so that none of them can hit any other in one move.(Source: http://www.math.utah.edu/~alfeld/queens/queens.html)

Here we are solv­ing it for N queens in NxN chess board.
http://algorithms.tutorialhorizon.com/backtracking-n-queens-problem/

input: N
output: list with N elements where each element is the row number of the queen for each column, row starts with 0
For example, for N = 4, solution = [1, 3, 0, 2]
"""


def matrix(n):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(0)
    return result


def mark_board(board, row, col, value):
    for i in range(len(board)):
        board[row][i] += value  # Mark row
        board[i][col] += value  # Mark col
        # Mark Diagonals
        if row + i < len(board) and col - i >= 0:
            board[row + i][col - i] += value
        if row - i >= 0 and col + i < len(board):
            board[row - i][col + i] += value
        if row + i < len(board) and col + i < len(board):
            board[row + i][col + i] += value
        if row - i >= 0 and col - i >= 0:
            board[row - i][col - i] += value


def is_marked(board, row, col):
    return board[row][col] > 0


def n_queens_chess(n, board):
    if n == 0:
        return []
    col = len(board) - n
    for i in range(len(board)):
        if is_marked(board, i, col):
            continue
        # print ("b n={} i={} board={}".format(n, i, board))
        mark_board(board, i, col, 1)
        # print ("a n={} i={} board={}".format(n, i, board))
        sub_list = n_queens_chess(n - 1, board)
        # print ("n={} i={} sublist={} board={}".format(n, i, sub_list, board))
        if len(sub_list) == n - 1:
            return [i] + sub_list
        mark_board(board, i, col, -1)
    return []


def assertListEquals(l1, l2):
    assert len([i for i, j in zip(l1, l2) if i == j]) > 0


r = n_queens_chess(4, matrix(4))
print ("Result = {}".format(r))
assertListEquals(r, [1, 3, 0, 2])
