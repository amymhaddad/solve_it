# Initial Solution - Use a string
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    letters = ""

    for char in sentence.lower():
        if char.isalpha() and char not in letters:
            letters += char
    return len(letters) == len(lowercase_letters)

"""
Pros: Simple to read and understand
Cons: Not efficient in terms of complexity. That's because strings are immutable in Python. Each time I concatentate strings, an entirely new string is created and the letter is added to it.
"""


###Solutions When Apply Looking Back Approaches###

# Approach 1: Solve problem with a different approach
# Approach 1 Solution - ASCII representation
from string import ascii_lowercase as lowercase_letters

ALPHA_LENGTH = 26


def is_pangram(sentence):
    total_letters = []
    for i in range(ALPHA_LENGTH):
        total_letters.append(0)

    for char in sentence.lower():
        if char.isalpha():
            letter_index = ord(char) - ord("a")
            total_letters[letter_index] = 1

    return sum(total_letters) == ALPHA_LENGTH

"""
Pros: Relatively simple to understand; more efficient in terms of time/space complexity; creative solution 
Cons: It's a bit verbose 
"""



# Approach 2: Add a contraint
# Approach 2 Solution - Solve the problem without using a data structure in the function
from string import ascii_lowercase as lowercase_letters


def is_pangram(sentence):
    for letter in lowercase_letters:
        if letter not in sentence.lower():
            return False
    return True

"""
Pros: Simple to read and understand; efficient: good use of time/space complecity
"""



# Approach 3: Study the code of others
# Approach 3 Solution 1 - Use a set()
from string import ascii_lowercase as lowercase_letters

ALPHA_LENGTH = 26


def is_pangram(sentence):
    sentence_letters = set()

    for letter in sentence.lower():
        if letter.isalpha():
            sentence_letters.add(letter)
    return sentence_letters == set(lowercase_letters)
"""
Pros: Efficient: good use of time/space complecity

"""



# Approach 3 Solution 2 - Use bitwise operators
ALPHA_LENGTH = 26


def is_pangram(sentence):
    total_letters = 0

    for i, char in enumerate(sentence):
        if char.isalpha():
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            total_letters = total_letters | bit_shift

    return 2 ** ALPHA_LENGTH - 1 == total_letters

"""
Pros: Efficient: good use of time/space complecity

"""


# Approach 4: Teach yourself: study your own code
# Approach 4 Solution - Use regular expressions and set comprehension

import re


def is_pangram(sentence):

    return (
        len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
    )

"""
Pros: Efficient: good use of time/space complecity
Cons: Hard to read with everything on one line and not all data are named.

"""


# Approach 4 Revised Solution
import re

ALPHA_LENGTH = 26


def is_pangram(sentence):
    letters = set()
    for letter in re.findall(r"[A-Za-z]", sentence.lower()):
        letters.add(letter)
    return len(letters) == ALPHA_LENGTH

"""
Pros: Efficient: good use of time/space complecity; simple to read and understand
"""
