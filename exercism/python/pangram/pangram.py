import re


# def is_pangram(sentence):
#
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
#     )

#Ch
#dictionary
from string import ascii_lowercase as lower
# def is_pangram(sentence):
#     alphabet = {letter:0 for letter in lower}
#
#     for character in sentence.lower():
#         if character.isalpha():
#             alphabet[character] = alphabet.get(character, 0) + 1
#     for letter, count in alphabet.items():
#         if count == 0:
#             return False
#     return True
#    
#Sort and compare
def is_pangram(sentence):
    if not sentence:
        return False

    phrase_letters = []

    for letter in sentence.lower():
        if letter.isalpha() and letter not in phrase_letters:
            phrase_letters.append(letter)

    phrase_letters.sort()
    return phrase_letters == list(lower)
#jsentence = "the quick brown fox jumps over the lazy dog"
#print(is_pangram(sentence))
