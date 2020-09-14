from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter

sentence = "go Go GO Stop stop"


def count_words(sentence):

    letters_digits = "[a-zA-Z\d]+'?[a-zA-Z]*"

    parsed_words = re.findall(letters_digits, sentence)

    case_insensitive_results = [word.lower() for word in parsed_words]

    return Counter(case_insensitive_results)


print(count_words(sentence))

# Counter({"go": 1, "Go": 1, "GO": 1, "Stop": 1, "stop": 1})


# \w+\'\w{1} -- contractions
# \'(\w+)\' -- quotes
# [a-zA-Z]+\'*[a-zA-Z]+\b --> One or more letters with optional apostrophy one or more letters with word boundary
# //[(\w+)|(\w+\'?\w)]
