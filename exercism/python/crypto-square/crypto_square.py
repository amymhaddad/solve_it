import re

# value = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
value = "This is fun"


def normalize_string(plain_text):

    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


chars = normalize_string(value)


def create_rectangle(chars):
    row = 0
    col = 1

    col_larger_eq_row = col >= row
    col_only_greater_by_one = col - row < -1
    min_length = row * col < len(chars)

    # I need to have some condintion to get the cols and rows to stop incrementing
    while True:
        

        if not col_larger_eq_row and not col_only_greater_by_one:
            col += 1

        row += 1
    return {"row": row, "column": col}
    # return row, col


print(create_rectangle(chars))
# while (col < row) or (col - row > 1):
#     row += 1
#         continue
#     col += 1
# return {"row": row, "column": col}


# rectangle = create_rectangle("thisisfun")

# print(rectangle)


# def parse_rectangle(rectangle, chars):

#     total_rows = []
#     start = 0
#     end = rectangle["column"]

#     while len(chars) - end > 1:
#         each_row = chars[start:end]
#         total_rows.append(each_row)
#         start = end
#         end += rectangle["column"]

#     total_rows.append(chars[start:])

#     return total_rows


# # rectangle = create_rectangle("ifmanwasmeanttostayonthegroundgodwouldhavegivenusrootsff")


# def encoded_words(parsed_rectangle):
#     print("p", parsed_rectangle)
#     cols = [list(col) for col in zip(*parsed_rectangle)]
#     return " ".join(["".join(word) + " " for word in cols])


# # encode = encoded_words(rectangle_with_parsed_words)
# # print(encode)
# def cipher_text(plain_text):

#     chars = normalize_string(plain_text)
#     if len(chars) <= 1:
#         return chars

#     else:
#         rectangle = create_rectangle(chars)
#         rectangle_with_parsed_words = parse_rectangle(rectangle, chars)
#         encode = encoded_words(rectangle_with_parsed_words)
#         return encode

