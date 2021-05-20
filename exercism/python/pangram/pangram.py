import re

#Import the lowercase letters from Ascii so I can easily check if a solution contains all letters 
from string import ascii_lowercase as lowercase_letters

#Create a global variable that's set to the length of the English alphabet. 
# That way, I can refer to this number throughout my program, if needed.
ALPHA_LENGTH = 26

# set - 3
def is_pangram(sentence):
    #Create an empty set that'll hold all of the letters from the given sentence. 
    #A set() holds unique elements, which what I want since I'm checking if a sentence contains all letters of the English alphabet
    sentence_letters = set()

    #Iterate through the given sentence and lowercase each character on each iteration. Lowercase each letter as a way to standardize the input.
    for letter in sentence.lower():
        #On each iteration, check if the charater is a letter in the alphabet. 
        # I need to add this check because I only want to compare the letter -- not numbers, spaces, or puncuation marks
        if letter.isalpha():
        #Add each letter to the set. Because a set only contains unique elements, I won't get any duplicates in my output.
            sentence_letters.add(letter)

    #Compare my set of sentence letters to a set of lowercase letters
    return sentence_letters == set(lowercase_letters)

"""
Key Points:
-set() - contains unique elements
-Standardize the given input to account for upper and lowercase letters in the given sentence
-Check only for letters in the given string, and ignore all other characters
"""




# set - 3
def is_pangram(sentence):
    sentence_letters = set()

    for letter in sentence.lower():
        if letter.isalpha():
            sentence_letters.add(letter)
    return sentence_letters == set(lowercase_letters)




# # set - 1
# def is_pangram(sentence):
#     ALPHA_LENGTH = 26
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)))
#         == ALPHA_LENGTH
#     )


# # set - 2
# def is_pangram(sentence):
#     return set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence)) == set(
#         lowercase_letters
#     )


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
#     total_letters = [0 for i in range(ALPHA_LENGTH)]

#     for i, char in enumerate(sentence.lower()):
#         if char.isalpha():
#             letter_index = ord(char) - ord("a")
#             total_letters[letter_index] = 1

#     return sum(total_letters) == ALPHA_LENGTH




def is_pangram(sentence):
    total_letters = 0

    for i, char in enumerate(sentence):
        if char.isalpha():
            #At each letter, get the current ascii val and subtract it from the start of the alphabet 
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            total_letters = total_letters | bit_shift
            print(bin(bit_shift), bin(total_letters))

    return 2**26-1 == total_letters


def is_pangram(sentence):
    total_letters = 0

    for i, char in enumerate(sentence):
        if char.isalpha():
            letter_index = ord(char.lower()) - ord("a")
            bit_shift = 1 << letter_index
            total_letters = total_letters | bit_shift

    return 2**26-1 == total_letters
