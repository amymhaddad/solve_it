from collections import Counter
import re


def count_words(sentence):
    letters_digits = "[a-zA-Z]+'[a-zA-Z]|[a-zA-Z\d]+"
    parsed_words = re.findall(letters_digits, sentence)
    return Counter([word.lower() for word in parsed_words])
