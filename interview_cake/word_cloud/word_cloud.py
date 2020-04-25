"""
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.
"""

from string import punctuation


def word_cloud_data(input):
    all_words = standardize_string(input)
    word_counter = {}
    for word in all_words.split():
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter


def standardize_string(input):

    punctuation_to_match = set("-'")

    all_words = ""

    for i, char in enumerate(input.lower()):

        if char.isalpha() or char.isspace():
            all_words += char

        elif char in punctuation:
            if i == len(input) - 1:
                break

            elif char in punctuation_to_match:
                if all_words[-1].isalpha() and input[i + 1].isalpha():
                    all_words += char
            else:
                all_words += " "
                continue
    return all_words
