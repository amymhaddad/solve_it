"""
Given a pattern and a wordsing words, find if words follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in words.

Example 1:

Input: pattern = "abba", words = "dog cat cat dog"
Output: true
"""


def word_pattern(pattern, words):

    words_as_list = words.split(" ")
    pattern_as_list = [letter for letter in pattern]

    if len(set(pattern)) != len(set(words_as_list)):
        return False
    if len(words_as_list) != len(pattern_as_list):
        return False

    map_letter_to_word = {}

    for i, letter in enumerate(pattern):
        if (
            letter not in map_letter_to_word
            and words_as_list[i] not in map_letter_to_word.values()
        ):
            map_letter_to_word[letter] = words_as_list[i]

    if len(map_letter_to_word.keys()) != len(set(pattern)):
        return False
    else:
        for i, letter in enumerate(pattern):
            if map_letter_to_word[letter] != words_as_list[i]:
                return False
        return True
