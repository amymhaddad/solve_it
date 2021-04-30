import re


# def is_pangram(sentence):
#
#     return (
#         len(set(letter.lower() for letter in re.findall(r"[A-Za-z]", sentence))) == 26
#     )

def is_pangram(sentence):
    letter_counter = {}

    for character in sentence:
        if character.isalpha():
            letter_counter[character] = letter_counter.get(character, 0) + 1

    print(letter_counter)

print(is_pangram("abceddd"))
