import re

"""
-Should all input be lower case so people don't have to deal w/mixed case?

"""

# def is_pangram(phrase):
#
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", phrase))) == 26
#     )

# Ch
# dictionary
from string import ascii_lowercase as lower

# def is_pangram(phrase):
#     alphabet = {letter:0 for letter in lower}
#
#     for character in phrase.lower():
#         if character.isalpha():
#             alphabet[character] = alphabet.get(character, 0) + 1
#     for letter, count in alphabet.items():
#         if count == 0:
#             return False
#     return True
#
# Sort and compare
# Hint: why do you think I use an array instead of setting phrase letters to a
# string?
# def is_pangram(phrase):
#     if not phrase:
#         return False
#
#     phrase_letters = []
#
# for letter in phrase.lower():
#     if letter.isalpha() and letter not in phrase_letters:
#         phrase_letters.append(letter)
#
# phrase_letters.sort()
# return phrase_letters == list(lower)
# jphrase = "the quick brown fox jumps over the lazy dog"
# print(is_pangram(phrase))

# set()
def is_pangram(phrase):
    if not phrase:
        return False
    alphabet_length = 26
    phrase_letters = set()

    for letter in phrase.lower():
        if letter.isalpha():
            phrase_letters.add(letter)

    return len(phrase_letters) == alphabet_length 
# array v2
# def is_pangram(sentence):
#     if not sentence:
#         return False

#     letters = list(lower)

#     for char in sentence.lower():
#         if char in letters:
#             letter_index = letters.index(char)
#             letters.pop(letter_index)
#     return len(letters) == 0


sentence = "abcdefghijklmnopqrstuvwxyz"
print(is_pangram(sentence))


#Use  ord()
#https://exercism.io/tracks/javascript/exercises/pangram/solutions?order=num_comments