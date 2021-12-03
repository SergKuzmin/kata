"""
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.
"""


def wave_gen(n):
    prev = None
    direction = 1
    while True:
        if prev is None:
            prev = -1
        elif prev == 0:
            direction = 1
        elif prev == n - 1:
            direction = -1
        prev += direction
        yield prev


def encode_rail_fence_cipher(string, n):
    if n > 0:
        result = [[] for _ in range(n)]
        for s, index in zip(string, wave_gen(n)):
            result[index].append(s)
        return ''.join(map(''.join, result))
    else:
        return string


def decode_rail_fence_cipher(string, n):
    if n > 0:
        num_in_part = [[] for _ in range(n)]
        for _, index in zip(string, wave_gen(n)):
            num_in_part[index].append(1)
        num_in_part = [0] + list(map(sum, num_in_part))[:-1]
        num_in_part = [sum(num_in_part[:i + 1]) for i in range(len(num_in_part))]
        slices = [(i, j) for i, j in zip(num_in_part[:-1], (num_in_part[1:]))]
        slices += [(slices[-1][-1], len(string))]
        parts = [list(string[i:j]) for i, j in slices]
        result = ''
        for _, index in zip(string, wave_gen(n)):
            result += parts[index].pop(0)
        return result
    else:
        return string


if __name__ == '__main__':
    string = ""

    print(encode_rail_fence_cipher(string, 33))
    print('H !e,Wdloollr')
    print(decode_rail_fence_cipher('H !e,Wdloollr', 4))
    print(string)
