"""
Implement an algorithm to determine if a string has all unique characters. What if you can't use additional data structures?
"""


from collections import Counter


string = "word"

# dictionary
def is_unique_approach_1(string):
    letter_counter = Counter()

    for letter in string:
        letter_counter[letter] += 1

    for letter, count in letter_counter.items():
        if count > 1:
            return False
    return True


# set version 1
def is_unique_approach_2(string):

    set_string = set({letter for letter in string})

    if len(set_string) != len(string):
        return False

    for letter in string:
        if letter not in set_string:
            return False
    return True


# set version 2
def is_unique_approach_3(string):
    return len(set(string)) == len(string)
