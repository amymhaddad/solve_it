import re


chars = "thisisfun"


def cipher_text(plain_text):
    if not plain_text:
        return ""
    else:
        return normalize_string(plain_text)


def normalize_string(plain_text):

    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


string = normalize_string(chars)


def create_rectangle(chars):
    r = 1
    c = 1

    while r * c < len(chars):
        if (c < r) or (c - r > 1):
            c += 1
            continue
        r += 1

    return {"row": r, "column": c}


rectangle = create_rectangle(string)


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


rectangle_with_parsed_words = parse_rectangle(rectangle)


def encoded_words(parsed_rectangle):

    cols = [list(col) for col in zip(*parsed_rectangle)]
    return "".join(["".join(word).replace(",", "") + "\n" for word in cols]).strip()


encode = encoded_words(rectangle_with_parsed_words)
print(encode)
