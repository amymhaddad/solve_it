from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter

sentence = ",\n,one,\n ,two \n 'three'"


def count_words(sentence):

    letters_digits = "[\w'?]+"
    remove_quotes = re.sub("\'\w\'")
    parsed_words = re.findall(letters_digits, sentence)

    case_insensitive_results = [word.lower() for word in parsed_words]

    return Counter(case_insensitive_results)


print(count_words(sentence))

# letters_digits = "[\b\w+\b]+"

# [(\w)|(w\'\w)|(\b\w+\b)]+
