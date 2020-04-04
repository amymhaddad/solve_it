"""
Write a function that takes a list of characters and reverses the letters in place.
"""

list_string = ["A", "B", "C", "D"]


def reverse(list_string):

    left = len(list_string) - 1
    right = 0

    if len(list_string) <= 1:
        return list_string

    while right < left:

        list_string[left], list_string[right] = (
            list_string[right],
            list_string[left],
        )

        right += 1
        left -= 1
    return list_string
