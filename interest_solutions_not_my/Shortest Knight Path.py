"""
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to
 the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should
 return 1.

The knight is not allowed to move off the board. The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output,
 and expected output; please post them.)
"""
from collections import deque
moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))


def knight(p1, p2):
    x, y = ord(p2[0])-97, int(p2[1])-1
    left, seen = deque([(ord(p1[0])-97, int(p1[1])-1, 0)]), set()
    while left:
        i, j, v = left.popleft()
        if i == x and j == y: return v
        if (i, j) in seen: continue
        seen.add((i, j))
        for a, b in moves:
            if 0 <= i+a < 8 and 0 <= j+b < 8:
                left.append((i+a, j+b, v+1))


if __name__ == '__main__':
    print(deque([1, 0]))
