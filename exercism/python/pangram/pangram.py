import re
from string import ascii_lowercase as lowercase_letters

# # set - 1
# def is_pangram(sentence):
#     alphabet_length = 26
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)))
#         == alphabet_length
#     )


# # set - 2
# def is_pangram(sentence):
#     return set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)) == set(
#         lowercase_letters
#     )


# set - 3
def is_pangram(sentence):
    sentence_letters = set()

    for letter in sentence.lower():
        if letter.isalpha():
            sentence_letters.add(letter)
            
    return sentence_letters == set(lowercase_letters)

# #set - 4
# def is_pangram(sentence):
#     letters = re.findall(r"[A-Za-z]", sentence.lower())
#     return set(lowercase_letters).issubset(set(letters))

# # dictionary
# def is_pangram(sentence):
#     alphabet = {letter: 0 for letter in lowercase_letters}

#     for character in sentence.lower():
#         if character.isalpha():
#             alphabet[character] = alphabet.get(character, 0) + 1

#     for letter, count in alphabet.items():
#         if count == 0:
#             return False
#     return True


# # Sort and compare
# def is_pangram(sentence):

#     sentence_letters = []

#     for character in sentence.lower():
#         if character.isalpha() and character not in sentence_letters:
#             sentence_letters.append(character)

#     sentence_letters.sort()
#     return sentence_letters == list(lowercase_letters)


# # array
# def is_pangram(sentence):

#     letters = list(lowercase_letters)

#     for char in sentence.lower():
#         if char in letters:
#             letter_index = letters.index(char)
#             letters.pop(letter_index)
#     return len(letters) == 0


# # array v2
# def is_pangram(sentence):
#     alphabet_length = 26
#     total_letters = [0 for i in range(alphabet_length)]

#     for i, char in enumerate(sentence):
#         if char.isalpha():
#             letter_index = ord(char.lower()) - ord("a")
#             total_letters[letter_index] = 1

#     return sum(total_letters) == alphabet_length
