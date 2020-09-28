def cipher_text(plain_text):
    if not plain_text:
        return ""
    else:
        return normalized_string(plain_text)


def normalized_string(plain_text):

    updated_string = ""

    for char in plain_text:
        if char.isalpha():
            updated_string += char.lower()
    return updated_string


# chars = "imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"

# for cols in range(9):
#     for row in range(cols):
#         if cols * row >= len(chars):
#             if cols > row:
#                 if cols - row <= 1:
#                     print(cols, row)
