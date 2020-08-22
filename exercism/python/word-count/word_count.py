from collections import Counter
from string import punctuation
from string import ascii_lowercase as alpha

sentence = "one,\ntwo,\nthree"


def count_words(sentence):

    # lowercase words
    valid_chars = ["'", "-"]

    start = 0
    i = 0

    words = []
    while i < len(sentence) - 1:
        # import pdb

        # pdb.set_trace()
        if sentence[i] not in valid_chars or sentence[i] not in alpha:
            i += 1
            start += 1
            continue

        while True:
            if sentence[i].isalpha():
                i += 1
                continue

            elif sentence[i] in valid_chars and sentence[i + 1].isalpha():
                i += 1
                continue

            else:
                words.append(sentence[start:i])
                i += 1
                start = i
                break
        words.append(sentence[start : i + 1])
    total_word_count = Counter(words)

    return total_word_count


print(count_words(sentence))


# start = 0
# i = 0

# words = []
# while i < len(sentence) - 1:
#     if sentence[i].isalpha():
#         i += 1
#         continue
#     elif sentence[i] in punctuation:
#         words.append(sentence[start:i])
#         i += 1
#         start = i
# words.append(sentence[start : i + 1])

# print(words)

