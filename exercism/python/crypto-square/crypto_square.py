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
#  self.rows = [[int(x) for x in xs.split()] for xs in M.splitlines()]
#         self.cols = [col for col in zip(*self.rows)]


def encoded_words(parsed_rectangle):
    cols = [list(col) for col in zip(*parsed_rectangle)]
    print(cols)

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


# cols = [list(col) for col in zip(*self.rows)]


class Matrix(object):
    def __init__(self, M):
        # self.rows = [[int(x) for x in xs.split()] for xs in M.splitlines()]
        self.rows = [
            ["i, f, m, a, n, w, a, s, "],
            ["m, e, a, n, t, t, o, s, "],
            ["t, a, y, o, n, t, h, e, "],
            ["g, r, o, u, n, d, g, o, "],
            ["d, w, o, u, l, d, h, a, "],
            ["v, e, g, i, v, e, n, u, "],
        ]
        self.cols = [col for col in zip(*self.rows)]


matrix = "89 1903 3\n18 3 1\n9 4 800"
# m = Matrix(matrix)
# print(m.rows)
# print(m.cols)
# # [[89, 1903, 3], [18, 3, 1], [9, 4, 800]]
