'''
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples

balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
'''


def balanced_parens(n):
    result = set()
    if n == 0:
        return ['']

    def build(r, l, state, string):
        if state >= 0:
            if r == 0:
                if state:
                    result.add(string + ')'*l)
            if r > 0:
                build(r-1, l, state + 1, string + '(')
                build(r, l-1, state - 1, string + ')')
    build(n-1, n, 1, '(')
    return list(result)

print(balanced_parens(3))


