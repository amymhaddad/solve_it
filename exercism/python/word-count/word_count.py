from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re

# sentence = "one,two,three"

from collections import Counter


def count_words(sentence):
    prog = "[a-zA-z0-9]+'?"
    result = re.findall(prog, sentence)

    return Counter(result)


# print(count_words(sentence))
