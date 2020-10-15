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
    stop = cols
    for i in range(rows):
        each_row = letters[start:stop]
        rect.append(each_row)
        start = stop
        stop += cols

    # cols = [list(col) for col in zip(*rect)]
    # updated_phrase = "".join(["".join(word) + " " for word in cols])
    # print(updated_phrase)
    #  encoded_rect = [[rect[row][col] for row in range(rows)] for col in range(cols)]
    nw = 0
    r = []
    encoded_word = ""
    for i in range(rows):
        # print(i)
        for col in rect:
            if len(encoded_word) > rows:
                r.append(encoded_word)
                encoded_word = ""
            else:
                encoded_word += col[nw]
                nw += 1
                continue

    print(r)
    # print(col[i])
    # for col in rect:
    #     print(col)


# ['i', 'm', 't', 'g', 'd', 'v', 's']
# ['f', 'e', 'a', 'r', 'w', 'e', 'r']
# ['m', 'a', 'y', 'o', 'o', 'g', 'o']
# ['a', 'n', 'o', 'u', 'u', 'i', 'o']
# ['n', 't', 'n', 'n', 'l', 'v', 't']
# ['w', 't', 't', 'd', 'd', 'e', 's']
# ['a', 'o', 'h', 'g', 'h', 'n', ' ']

# (['i', 'f', 'm', 'a', 'n', 'w', 'a', 's'],)
# (['m', 'e', 'a', 'n', 't', 't', 'o', 's'],)
# (['t', 'a', 'y', 'o', 'n', 't', 'h', 'e'],)
# (['g', 'r', 'o', 'u', 'n', 'd', 'g', 'o'],)
# (['d', 'w', 'o', 'u', 'l', 'd', 'h', 'a'],)
# (['v', 'e', 'g', 'i', 'v', 'e', 'n', 'u'],)
# (['s', 'r', 'o', 'o', 't', 's', ' '],)


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

