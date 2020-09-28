from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter

sentence = "go Go GO she'd Stop stop won't 'large' and large"


def count_words(sentence):

    # contractions = "[a-zA-Z\d]+ | [a-zA-Z]+'[a-zA-Z]"

    letters_digits = "[a-zA-Z]+'[a-zA-Z] | [a-zA-Z\d]+"

    parsed_words = re.findall(letters_digits, sentence)
    print(parsed_words)

    # case_insensitive_results = [word.lower() for word in parsed_words]

    # return Counter(case_insensitive_results)


print(count_words(sentence))

# Counter({"go": 1, "Go": 1, "GO": 1, "Stop": 1, "stop": 1})


# \w+\'\w{1} -- contractions
# \'(\w+)\' -- quotes
# [a-zA-Z]+\'*[a-zA-Z]+\b --> One or more letters with optional apostrophy one or more letters with word boundary
# //[(\w+)|(\w+\'?\w)]
