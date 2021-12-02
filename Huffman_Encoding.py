"""
Motivation

Natural language texts often have a very high frequency of certain letters, in German for example, almost every 5th letter is an E, but only every 500th is a Q. It would then be clever to choose a very small representation for E. This is exactly what the Huffman compression is about, choosing the length of the representation based on the frequencies of the symbol in the text.

Algorithm

Let's assume we want to encode the word "aaaabcc", then we calculate the frequencies of the letters in the text:

Symbol	Frequency
a	4
b	1
c	2
Now we choose a smaller representation the more often it occurs, to minimize the overall space needed. The algorithm uses a tree for encoding and decoding:

  .
 / \
a   .
   / \
   b  c
Usually we choose 0 for the left branch and 1 for the right branch (but it might also be swapped). By traversing from the root to the symbol leaf, we want to encode, we get the matching representation. To decode a sequence of binary digits into a symbol, we start from the root and just follow the path in the same way, until we reach a symbol.

Considering the above tree, we would encode a with 0, b with 10 and c with 11. Therefore encoding "aaaabcc" will result in 0000101111.

(Note: As you can see the encoding is not optimal, since the code for b and c have same length, but that is topic of another data compression Kata.)

Tree construction

To build the tree, we turn each symbol into a leaf and sort them by their frequency. In every step, we remove 2 trees with the smallest frequency and put them under a node. This node gets reinserted and has the sum of the frequencies of both trees as new frequency. We are finished, when there is only 1 tree left.

(Hint: Maybe you can do it without sorting in every step?)

Goal

Write functions frequencies, encode and decode.

Note: Frequency lists with just one or less elements should get rejected. (Because then there is no information we could encode, but the length.)
"""


class Node:
    def __init__(self, left= None, right=None):
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get(self, num):
        if num == 0:
            return self.left
        else:
            return self.right

    # def __str__(self):
    #     return f"\n" \
    #            f"{self.left} {self.right}"


    # takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    s_list = list(s)
    unique_char = set(s_list)
    char_num = sorted([(char, s_list.count(char)) for char in unique_char],
                      key=lambda x: x[1], reverse=True)

    result = []
    for i, (char, _) in enumerate(char_num):
        if i != len(char_num) - 1:
            result.append((char, int(i*'1' + '0')))
        else:
            result.append((char, int(i * '1')))

    return result


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    char_int = dict(freqs)
    return ''.join([str(char_int[char]) for char in s])


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    freqs = sorted(freqs, key=lambda x: x[1])
    array = [Node() for _ in range(len(freqs) - 1)]
    tree = array[0]
    for i, node in enumerate(array):
        node.set_left(freqs[i][0])
        if str(freqs[i + 1][1])[-1] == '0':
            node.set_right(array[i+1])
        else:
            node.set_right(freqs[i+1][0])

    result = ''
    tmp = tree

    for i in str(bits):
        tmp = tmp.get(int(i))
        if isinstance(tmp, str):
            result += tmp
            tmp = tree

    return result


if __name__ == '__main__':
    string = 'aaaaabbvvcsaaasddddd'
    print(string)
    print(frequencies(string))
    print(encode(frequencies(string), string))
    print(decode(frequencies(string), encode(frequencies(string), string)))