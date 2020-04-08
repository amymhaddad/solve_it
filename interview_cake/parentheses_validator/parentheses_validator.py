"""
Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False
"""


PARENS_DICT = {
    "{": "}",
    "[": "]",
    "(": ")",
}


# Approach 1: use a list as a stack
def multi_parens_approach_1(parens):
    stack = []
    for paren in parens:
        if paren in PARENS_DICT.keys():
            stack.append(paren)
        else:
            if len(stack) < 1:
                return False
            else:
                last_item = stack[-1]
                if PARENS_DICT[last_item] == paren:
                    stack.pop()
                else:
                    return False
    return len(stack) == 0


# Approach 2: use the stack class
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


def multi_parens_approach_2(parens):
    stack = Stack()
    for paren in parens:
        if paren in PARENS_DICT.keys():
            stack.push(paren)
        else:
            last_paren = stack.peek()
            if PARENS_DICT[last_paren] == paren:
                stack.pop()
            else:
                return False
    return stack.is_empty()
