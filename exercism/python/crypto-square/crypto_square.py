import re

value = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
# value = "This is fun"


def normalize_string(plain_text):

    letters = [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]

    cols, rows = create_rectangle(letters)

    spaces_needed = cols * rows - len(letters)
    if spaces_needed:
        letters.append(" ")

    rect = []
    start = 0
    stop = rows
    for i in range(rows):
        each_row = letters[start:stop]
        rect.append(each_row)
        start = stop
        stop += rows

    return rect

    #     pdb.set_trace()
    # rect = [letters[cols * i : cols * i + rows + 1] for i in range(rows)]
    # encoded_rect = [[rect[row][col] for row in range(rows)] for col in range(cols)]


def create_rectangle(chars):

    col = 1
    while True:
        row = col - 1
        for num in range(2):
            if (row * col >= len(chars)) and col >= row and col - row <= 1:
                return col, row
            else:
                row += 1
        col += 1
    return col, row


print(normalize_string(value))
# rectangle = create_rectangle(chars)


# def rows(rectangle, chars):

#     start = 0
#     matrix = []

#     col, row = rectangle
#     rect_length = col * row

#     each_row = ""
#     for i in range(col * row):

#         if i >= len(chars):
#             each_row += " "
#             continue
#         else:
#             each_row += chars[i]

#         if len(each_row) == col:
#             matrix.append(each_row)
#             each_row = ""
#     if each_row:
#         matrix.append(each_row)
#     return matrix


# all_rows = rows(rectangle, chars)


# def encoded_words(all_rows):
#     cols = [list(col) for col in zip(*all_rows)]
#     updated_phrase = "".join(["".join(word) + " " for word in cols])

# print(encoded_words(all_rows))


# def cipher_text(plain_text):

#     chars = normalize_string(plain_text)
#     if len(chars) <= 1:
#         return chars

#     else:
#         rectangle = create_rectangle(chars)
#         all_rows = rows(rectangle, chars)
#         return encoded_words(all_rows)
# rectangle = create_rectangle(chars)
# rectangle_with_parsed_words = parse_rectangle(rectangle, chars)
# encode = encoded_words(rectangle_with_parsed_words)
# return encode

#

