import re

from string import ascii_lowercase as lowercase_letters


ALPHA_LENGTH = 26


def is_pangram(sentence):
    total_letters = {}

    for char in sentence.lower():
        if char.isalpha():
            letter_index = ord(char) - ord("a")
            total_letters[letter_index] = 1

    return len(total_letters) == ALPHA_LENGTH


# a --> 97
# b --> 98
# c --> 99
# d --> 100


# a --> 0
# b --> 1
# c --> 2
# d --> 3
# ...
# z --> 25


# String
def is_pangram(sentence):
    letters = ""

    for char in sentence.lower():
        if char.isalpha() and char not in letters:
            letters += char
    return len(letters) == len(lowercase_letters)


# set - 3
def is_pangram(sentence):
    sentence_letters = set()

    for letter in sentence.lower():
        if letter.isalpha():
            sentence_letters.add(letter)
    return sentence_letters == set(lowercase_letters)


# set - 1
def is_pangram(sentence):
    ALPHA_LENGTH = 26
    return (
        len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)))
        == ALPHA_LENGTH
    )


# set - 2
def is_pangram(sentence):
    return set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)) == set(
        lowercase_letters
    )


# Regex
def is_pangram(sentence):
    letters = set()
    for letter in re.findall(r"[A-Za-z]", sentence):
        letters.add(letter)
    return len(letters) == ALPHA_LENGTH


# set - 4
def is_pangram(sentence):
    letters = re.findall(r"[A-Za-z]", sentence.lower())
    return set(lowercase_letters).issubset(set(letters))


# dictionary
def is_pangram(sentence):
    alphabet = {letter: 0 for letter in lowercase_letters}

    for character in sentence.lower():
        if character.isalpha():
            alphabet[character] += 1

    for count in alphabet.values():
        if count == 0:
            return False
    return True


# Sort and compare
def is_pangram(sentence):

    sentence_letters = []

    for character in sentence.lower():
        if character.isalpha() and character not in sentence_letters:
            sentence_letters.append(character)

    sentence_letters.sort()
    return sentence_letters == list(lowercase_letters)


# array
def is_pangram(sentence):

    letters = list(lowercase_letters)

    for char in sentence.lower():
        if char in letters:
            letter_index = letters.index(char)
            letters.pop(letter_index)
    return len(letters) == 0


# # array v2
def is_pangram(sentence):
    total_letters = []
    for i in range(ALPHA_LENGTH):
        total_letters.append(0)

    for char in sentence.lower():
        if char.isalpha():
            letter_index = ord(char) - ord("a")
            total_letters[letter_index] = 1

    return sum(total_letters) == ALPHA_LENGTH


def is_pangram(sentence):
    total_letters = 0

    for i, char in enumerate(sentence):
        if char.isalpha():
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            total_letters = total_letters | bit_shift

    return 2 ** 26 - 1 == total_letters


##study

# def is_pangram(sentence):
#     total_letters = 0

#     for i, char in enumerate(sentence):
#         if char.isalpha():
#             #At each letter, get the current ascii val and subtract it from the start of the alphabet
#             letter_index = ord(char.lower()) - ord("a")
#             bit_shift = 1 << letter_index
#             total_letters = total_letters | bit_shift
#             print(bin(bit_shift), bin(total_letters))

#     return 2**26-1 == total_letters


"""
Iterate through the lowercase_letters. See if each letter is in the test string

"""


def is_pangram(sentence):
    for letter in lowercase_letters:
        if letter not in sentence.lower():
            return False
    return True


print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))
