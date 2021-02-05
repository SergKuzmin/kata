'''
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Calculator.new.evaluate("2 / 2 + 3 * 4 - 6") # => 7
Calculator.evaluate("2 / 2 + 3 * 4 - 6") // => 7
Calculator.evaluate "2 / 2 + 3 * 4 - 6" // => 7.0
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
'''

import operator
OP_D = {'/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub}
OP_LST = [{'/', '*'}, {'-', '+'}]

class Calculator(object):
    def evaluate(self, s):
        lst = s.split()
        print(lst)
        for preceed in range(2):
            i = 0
            while i < len(lst):
                if lst[i] in OP_LST[preceed]:
                    lst[i-1] = OP_D[ lst[i] ](float(lst.pop(i-1)), float(lst.pop(i)) )
                else:
                    i+=1
        return round(float(lst[0]), 10)
        
