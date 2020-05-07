"""
Write a recursive function for generating all permutations of an input string. Return them as a set.
"""


def get_permutations(string):

    if not string or len(string) == 1:
        return set(string)

    letters = set(string)

    permutations = set()

    for letter in letters:

        word_permutations = get_permutations(string[1:])
        for word in word_permutations:
            permutations.add(letter + word)
    return permutations
