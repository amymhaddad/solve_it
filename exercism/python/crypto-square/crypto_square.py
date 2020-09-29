value = "This is fun!"
import re


def cipher_text(plain_text):
    if not plain_text:
        return ""
    else:
        return normalized_string(plain_text)


def normalized_string(plain_text):

    updated_string = ""

    for char in plain_text:
        if char.isalpha() or char.isdigit():
            updated_string += char.lower()
    return updated_string


chars = "thisisfun"


def create_rectangle(chars):
    normalized_string_length = len(chars)

    r = 1
    c = 1

    while r * c < len(chars):
        if (c < r) or (c - r > 1):
            c += 1
            continue
        r += 1
    return {"row": r, "column": c}


rectangle = create_rectangle(chars)


def parse_rectangle(rectangle):
    total_rows = []
    start = 0
    end = rectangle["column"]

    while end <= len(chars):
        each_row = []
        for letter in chars[start:end]:
            each_row.append(letter)
        total_rows.append(each_row)
        start = end
        end += rectangle["column"]

    return total_rows


parsed_rectangle = parse_rectangle(rectangle)


def encoded_words(parsed_rectangle):

    cols = [list(col) for col in zip(*parsed_rectangle)]
    return "".join(["".join(word).replace(",", "") + "\n" for word in cols]).strip()

    # decoded_words = ""
    # for word in cols:
    #     decoded_words += "".join(word).replace(",", "") + "\n"

    # print(decoded_words)


print(encoded_words(parsed_rectangle))
