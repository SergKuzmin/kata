"""
If n is the numerator and d the denominator of a fraction, that fraction is defined a (reduced) proper fraction if and only if GCD(n,d)==1.

For example 5/16 is a proper fraction, while 6/16 is not, as both 6 and 16 are divisible by 2, thus the fraction can be reduced to 3/8.

Now, if you consider a given number d, how many proper fractions can be built using d as a denominator?

For example, let's assume that d is 15: you can build a total of 8 different proper fractions between 0 and 1 with it: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15, 13/15 and 14/15.

You are to build a function that computes how many proper fractions you can build with a given denominator:

proper_fractions(1)==0
proper_fractions(2)==1
proper_fractions(5)==4
proper_fractions(15)==8
proper_fractions(25)==20
Be ready to handle big numbers.

Edit: to be extra precise, the term should be "reduced" fractions, thanks to girianshiido for pointing this out and sorry for the use of an improper word :)
"""
import math
from itertools import combinations
from functools import reduce


def all_delim(n):
    last = n
    result = []
    while last != 1:
        finde = False
        for i in range(2, int(math.sqrt(last) + 1)):
            if last % i == 0:
                result.append(i)
                last = int(last / i)
                finde = True
                break
        if not finde:
            result.append(last)
            break
    return sorted(result)


def proper_fractions(n):
    if n == 1:
        return 0
    set_delim = sorted(set(all_delim(n)))
    result = n
    for i, d in enumerate(set_delim):
        result -= n // d
        for j in range(i+1):
            sign = (-1)**(j + 1)
            for comb in combinations(set_delim[:i], j):
                if comb:
                    result = result + (sign * n//(reduce(lambda x, y: x * y, comb) * d))
    return result


if __name__ == '__main__':
    print(proper_fractions(2631537))
    print(1754352.0)
