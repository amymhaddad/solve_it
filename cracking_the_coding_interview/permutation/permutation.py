"""
Given 2 strings, write a method to decide if one is a permutation of another.
"""

from collections import Counter


def is_permutation_approach_1(s1, s2):
    return Counter(s1) == Counter(s2)


def is_permutation_approach_2(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    common_elements = set1.intersection(set2)
    return common_elements == set1 and common_elements == set2


def is_permutation_approach_3(s1, s2):
    return sorted(s1) == sorted(s2)
