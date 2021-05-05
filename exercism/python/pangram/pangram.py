import re
from string import ascii_lowercase as lowercase_letters

# set
def is_pangram(sentence):
    return (
        len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
    )


# set()
def is_pangram(sentence):

    alphabet_length = 26
    sentence_letters = set()

    for letter in sentence.lower():
        if letter.isalpha():
            sentence_letters.add(letter)

    return len(sentence_letters) == alphabet_length


# dictionary
def is_pangram(sentence):
    alphabet = {letter: 0 for letter in lowercase_letters}

    for character in sentence.lower():
        if character.isalpha():
            alphabet[character] = alphabet.get(character, 0) + 1
    for letter, count in alphabet.items():
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
