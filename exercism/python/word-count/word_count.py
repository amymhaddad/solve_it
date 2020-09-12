from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter

sentence = "One,\nTwo,\nthree"


def count_words(sentence):

    letters_digits = "[\w'?]+"
    parsed_words = re.findall(letters_digits, sentence)

    case_insensitive_results = [word.lower() for word in parsed_words]

    return Counter(case_insensitive_results)


# print(count_words(sentence))


# def validate_data(sentence):
#     return " ".join([letter.lower() for letter in sentence.split() if letter.isalpha()])


# print(validate_data(sentence))
