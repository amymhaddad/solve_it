"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

"""

from collections import Counter


def uncommon_words(s1, s2):

    s1_count = Counter(s1.split())
    s2_count = Counter(s2.split())

    total_unique_s1 = [
        word for word, count in s1_count.items() if count == 1 and word not in s2_count
    ]

    total_unique_s2 = [
        word for word, count in s2_count.items() if count == 1 and word not in s1_count
    ]

    total_unique_s1.extend(total_unique_s2)
    return total_unique_s1
