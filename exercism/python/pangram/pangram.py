import re


# def is_pangram(sentence):
#
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
#     )

#dictionary
from string import ascii_lowercase as lower
def is_pangram(sentence):
    alphabet = {letter:0 for letter in lower}

    for character in sentence.lower():
        if character.isalpha():
            alphabet[character] = alphabet.get(character, 0) + 1
    for letter, count in alphabet.items():
        if count == 0:
            return False
    return True
    


