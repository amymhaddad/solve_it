import re


def normalize_string(plain_text):
    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


# string = normalize_string(chars)


def create_rectangle(chars):
    row = 1
    col = 1

    while row * col <= len(chars):
        if (col < row) or (col - row > 1):
            row += 1
            continue
        col += 1
    return {"row": row, "column": col}


# rectangle = create_rectangle(string)
# print(rectangle)


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
    cols = [["".join(word)] for word in parsed_rectangle]

    i = 0
    new_words = []
    for cols in zip(*cols):
        for word in cols:

            x = list(word)
            new_words.append(x[i])
            # print(x[i])
        i += 1
    print(new_words)
    # x = "".join(["".join(word) + " " for word in cols]).strip()


# encode = encoded_words(rectangle_with_parsed_words)
# print(encode)
def cipher_text(plain_text):
    if not plain_text:
        return ""
    else:
        chars = normalize_string(plain_text)
        rectangle = create_rectangle(chars)
        print(rectangle)
        rectangle_with_parsed_words = parse_rectangle(rectangle, chars)
        encode = encoded_words(rectangle_with_parsed_words)
        return encode


print(
    cipher_text(
        "If man was meant to stay on the ground, god would have given us roots."
    )
)
# print(cipher_text("clu hlt io "))
# cl hl io

# imtgdv fearwe mayoog anouui ntnnlv wttdde aohghn sseoau
