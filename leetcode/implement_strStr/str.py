"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""


def find_index_approach_a(haystack, needle):
    return haystack.find(needle)

