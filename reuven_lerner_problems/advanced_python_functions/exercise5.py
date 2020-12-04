"""
(2) Write a function ("getitems") that takes any number of arguments.
    It returns a function that takes a sequence as an argument.  That
    inner function then returns a tuple containing elements of its
    sequence at those indexes.

    For example:

    f = getitems(2, 4, 3)
    f('abcdefg')   # returns ('c', 'e', 'd')
    f('uvwxyz')   # returns ('w', 'y', 'x')

    f([10, 20, 30, 40, 50, 60, 70])  # returns (30, 50, 40)
    """


def get_items(*args):
    def sequence(seq):
        return tuple([seq[arg] for arg in args])

    return sequence


f = get_items(2, 4, 3)
print(f("abcdefg"))  # returns ('c', 'e', 'd')
print(f("uvwxyz"))  # returns ('w', 'y', 'x')
