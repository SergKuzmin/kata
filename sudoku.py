import time


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    def col_set(i):
        return set([puzzle[j][i] for j in range(9)])

    def row_set(i):
        return set(puzzle[i])

    def cub_set(i, j):
        return set([puzzle[i * 3 + k][j * 3 + l]
                    for k in range(3)
                    for l in range(3)])

    def get_cub_set(i, j):
        return cub_set(i // 3, j // 3)

    dict_of_row_sum = {i: row_set(i) for i in range(9)}
    dict_of_col_sum = {i: col_set(i) for i in range(9)}
    dict_of_cub_sum = {(i, j): cub_set(i, j)
                       for i in range(3)
                       for j in range(3)}
    while True:
        n = 0
        for i in range(81):
            x, y = i // 9, i % 9
            if puzzle[x][y] == 0:
                set_ = set()
                set_.update(col_set(y), row_set(x), get_cub_set(x, y))
                if len(set_) == 9 and (0 in set_):
                    for m in range(1, 10):
                        if m not in set_:
                            puzzle[x][y] = m
                            dict_of_row_sum[x].add(m)
                            dict_of_col_sum[y].add(m)
                            dict_of_cub_sum[(x // 3, y // 3)].add(m)
                            break
            else:
                n += 1
        if n == 81:
            break
    return puzzle


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# start = time.time()
# puzzle = sudoku(puzzle)
# print(time.time() - start)
#
# start = time.time()
# puzzle = sudoku(puzzle)
# print(time.time() - start)

from itertools import product


def possibles(puzzle, x, y):
    a, b = 3 * (x // 3), 3 * (y // 3)
    square = set([puzzle[r][c] for r, c in product(range(a, a + 3), range(b, b + 3))])
    row = set(puzzle[x])
    col = set(list(zip(*puzzle))[y])
    return set(range(1, 10)).difference(square.union(row).union(col))


def sudoku(puzzle):
    z = [(r, c) for (r, c) in product(range(9), range(9)) if puzzle[r][c] == 0]
    if z == []:
        return puzzle
    for (r, c) in z:
        p = possibles(puzzle, r, c)
        if len(p) == 1:
            puzzle[r][c] = p.pop()
    return sudoku(puzzle)


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

start = time.time()
a = [(i, j) for i in range(1_000) for j in range(1_000)]
print(time.time() - start)

# start = time.time()
# a = None
# print(time.time() - start)

start = time.time()
b = [(i, j) for i, j in product(range(1_000), range(1_000))]
print(time.time() - start)

# a = range(10)*range(10)
# print(a)
