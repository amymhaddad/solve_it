"""
Write a method to replace all spaces in a string wih "%20". You may assume taht the string has sufficient space at the end to hold the characters and you are given the "true" length of the string.

Example:
Input "Mr. John Smith     ", 13
Output: "Mr%20John%20Smith"

"""


def add_characters_to_string(string, length):
    pointer1 = length - 1
    characters = list(string)
    pointer2 = len(characters) - 1

    while pointer1 < pointer2:
        letter = characters[pointer1].isalpha()
        if letter:
            characters[pointer1], characters[pointer2] = (
                characters[pointer2],
                characters[pointer1],
            )
            pointer1 -= 1
            pointer2 -= 1

        space = characters[pointer1].isspace()
        if space:
            characters_to_add = "%20"
            characters[pointer2 - 2 : pointer2 + 1] = characters_to_add
            pointer2 -= 3
            pointer1 -= 1
    return "".join(characters)
