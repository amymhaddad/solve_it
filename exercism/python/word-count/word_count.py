from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha
import re


from collections import Counter


def count_words(sentence):

    letters_digits = "[\w'?]+"
    result = re.findall(letters_digits, sentence)

    return Counter(result)

