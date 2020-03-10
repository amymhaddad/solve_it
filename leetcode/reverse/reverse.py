"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


def reverse_s(string):
    end = len(string) - 1

    for i, letter in enumerate(string):
        if end - i < 1:
            break

        string[i], string[end] = string[end], string[i]
        end -= 1
    return string
