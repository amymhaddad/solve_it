"""
Write a generate that return the elements of its inputs one at a time. The generator can take any number of sequences. 
And if they aren't the same length, then the shortest one determines when things stop.
"""

import itertools as it

# Solution 1 - zip_longest
def zipgen_v1(*args):
    for char in it.zip_longest(*args):
        if None not in char:
            each_row = "".join(map(str, char))
            yield each_row


# Solution 2 - zip
def zipgen_v2(*args):
    for chars in zip(*args):
        for char in chars:
            yield char


# Solution 3 - zip with generator expression
def zipgen_v3(*args):
    return (char for chars in zip(*args) for char in chars)


if __name__ == "__main__":

    letters = "abcde"
    numbers = [1, 2, 3, 4, 5]
    symbols = "!@#$%"

    for one_item in zipgen_v3(letters, numbers, symbols):
        print(one_item)
