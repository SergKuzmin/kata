"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled
out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""


class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.n = len(self.data)

    def is_valid(self):
        try:
            a = int(self.n ** 0.5)
            assert (a * a == self.n)
            rows = {i: row for i, row in enumerate(self.data)}
            cols = {i: cols for i, cols in enumerate(zip(*self.data))}
            assert (len(rows) != 0)
            if len(rows) == 1:
                assert(rows[0][0] is not True)
            cubs = {(i, j): [self.data[a * i + k][a * j + l]
                             for k in range(a) for l in range(a)]
                    for i in range(a) for j in range(a)}
            for key, val in rows.items():
                assert (set(val) == set([i for i in range(1, self.n + 1)]))
                assert (len(val) == self.n)
            for key, val in cols.items():
                assert (set(val) == set([i for i in range(1, self.n + 1)]))
                assert (len(val) == self.n)
            for key, val in cubs.items():
                assert (set(val) == set([i for i in range(1, self.n + 1)]))
                assert (len(val) == self.n)
            return True
        except Exception as _:
            return False


# Valid Sudoku
goodSudoku1 = Sudoku([[True]
])

goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4],
])

# Invalid Sudoku
badSudoku1 = Sudoku([
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])

badSudoku2 = Sudoku([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1]
])

# Test.it('should be valid')
assert (goodSudoku1.is_valid() == True)
assert (goodSudoku2.is_valid() == True)
assert (badSudoku1.is_valid() == False)
assert (badSudoku2.is_valid() == False)
