import re

# def cipher_text(plain_text):
#     if not plain_text:
#         return ""
#    chars = normalize_string(plain_text)
#    rectangle = create_rectangle(chars)
#    rectangle_with_parsed_words = parse_rectangle(rectangle)
#    encode = encoded_words(rectangle_with_parsed_words)
#    return encode


def normalize_string(plain_text):

    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


# string = normalize_string(chars)


def create_rectangle(chars):
    r = 1
    c = 1

    while r * c < len(chars):
        if (c < r) or (c - r > 1):
            c += 1
            continue
        r += 1

    return {"row": r, "column": c}


# rectangle = create_rectangle(string)


def parse_rectangle(rectangle, chars):
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


# rectangle_with_parsed_words = parse_rectangle(rectangle)


def encoded_words(parsed_rectangle):

    cols = [list(col) for col in zip(*parsed_rectangle)]
    return "".join(["".join(word).replace(",", "") + " " for word in cols]).strip()


# encode = encoded_words(rectangle_with_parsed_words)
# print(encode)
def cipher_text(plain_text):
    if not plain_text:
        return ""
    else:
        chars = normalize_string(plain_text)
        rectangle = create_rectangle(chars)
        rectangle_with_parsed_words = parse_rectangle(rectangle, chars)
        encode = encoded_words(rectangle_with_parsed_words)
        return encode


# print(cipher_text("This is fun!"))
