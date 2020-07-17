"""
Implement a method to perform basic string compression using the counts of repeated characters. 

For example, the string aabbcccccaaa would become a2b1c5a3.

If the "compressed_string" string would not become smaller than the original string, your method should return the original string.
"""


def compress(string):
    left_pointer = 0
    count = 0
    compressed_string = []

    for right_pointer, letter in enumerate(string):
        if string[left_pointer] != string[right_pointer]:
            compressed_string.extend(string[left_pointer] + str(count))
            left_pointer = right_pointer
            count = 1
        else:
            count += 1

    compressed_string.extend(string[left_pointer] + str(count))
    if len(compressed_string) < len(string):
        return "".join(compressed_string)
    else:
        return string
