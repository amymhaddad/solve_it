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


def encoded_words(parsed_rectangle):
    print("p", parsed_rectangle)
    cols = [list(col) for col in zip(*parsed_rectangle)]
    return " ".join(["".join(word) + " " for word in cols])


# encode = encoded_words(rectangle_with_parsed_words)
# print(encode)
def cipher_text(plain_text):

    chars = normalize_string(plain_text)
    if len(chars) <= 1:
        return chars

    else:
        rectangle = create_rectangle(chars)
        rectangle_with_parsed_words = parse_rectangle(rectangle, chars)
        encode = encoded_words(rectangle_with_parsed_words)
        return encode


value = "This is fun!"
expected = "tsf hiu isn"
print(cipher_text(value))
