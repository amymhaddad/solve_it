"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

"""


def generate_string(n):
    if n == 1:
        return "a"
    elif n == 2:
        return "ab"
    elif n % 2 != 0:
        return n * "a"
    else:
        return (n - 1) * "a" + "b"
