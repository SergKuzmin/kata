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

alfa_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
num_alfa = {val: key for key, val in alfa_num.items()}
num_num = {val: val for key, val in alfa_num.items()}


def add_to_result(result: set, a, i):
    if (a is None) or (i is None):
        pass
    else:
        result.add(f'{a}{i}')


def get_all_possible_positions(p, result: set):
    ap, ip = list(p)
    ip = int(ip)
    for i in ['left', 'right', 'up', 'down']:
        for j in [+1, -1]:
            if i == 'left':
                add_to_result(result,
                              num_alfa.get(alfa_num[ap] - 2),
                              num_num.get(ip + j))
            elif i == 'right':
                add_to_result(result,
                              num_alfa.get(alfa_num[ap] + 2),
                              num_num.get(ip + j))
            elif i == 'up':
                add_to_result(result,
                              num_alfa.get(alfa_num[ap] + j),
                              num_num.get(ip + 2))

            elif i == 'down':
                add_to_result(result,
                              num_alfa.get(alfa_num[ap] + j),
                              num_num.get(ip - 2))
    return result


def knight(p1, p2):
    result = {p1}
    i = 0
    while True:
        i += 1
        tmp = result.copy()
        for p in tmp:
            get_all_possible_positions(p, result)
        if p2 in result:
            return i
