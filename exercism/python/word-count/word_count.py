from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter

sentence = ",\n,one,\n ,two \n 'three'"


def count_words(sentence):

    letters_digits = "[\w'?]+"

    parsed_words = re.findall(letters_digits, sentence)

    case_insensitive_results = [word.lower() for word in parsed_words]

    return Counter(case_insensitive_results)


print(count_words(sentence))


# \w+\'\w{1} -- contractions
#\'(\w+)\' -- quotes
# [a-zA-Z]+\'*[a-zA-Z]+\b --> One or more letters with optional apostrophy one or more letters with word boundary