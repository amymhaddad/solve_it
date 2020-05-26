"""
Write a recursive function for generating all permutations of an input string. Return them as a set.
"""


def get_permutations(string):

    if not string or len(string) == 1:
        return set(string)

    letters = set(string)

    permutations = set()

    for letter in letters:
        word_permutations = get_permutations(letters - set(letter))
        for permutation in word_permutations:
            permutations.add(letter + permutation)
    return permutations
