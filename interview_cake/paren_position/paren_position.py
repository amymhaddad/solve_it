"""
Write a function that, given a sentence, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
"""


OPEN_PAREN = "("
CLOSED_PAREN = ")"


# Version 1
def find_position(sentence, opening_paren_index):
    open_paren_count = 0

    for i in range(opening_paren_index + 1, len(sentence)):
        char = sentence[i]

        if char == OPEN_PAREN:
            open_paren_count += 1
        elif char == CLOSED_PAREN:
            if open_paren_count == 0:
                return i
            else:
                open_paren_count -= 1


# Version 2:
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


s1 = Stack()
s2 = Stack()


def find_position(parens, num):
    i = 0

    if len(parens) % 2 != 0:
        raise ValueError("You have unbalanced parens.")

    for paren in parens:
        if paren == OPEN_PAREN:
            if i <= num:
                s1.push(paren)
            else:
                s2.push(paren)
            i += 1
            continue

        if paren != OPEN_PAREN:
            if i < num:
                s1.pop()
                i += 1
                continue
            else:
                if not s2.is_empty():
                    s2.pop()
                    i += 1
                    continue
    return i
