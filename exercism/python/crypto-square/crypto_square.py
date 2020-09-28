value = "This is fun!"


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


print(cipher_text(value))

chars = "thisisfun"


def rectangle(chars):
    normalized_string_length = len(chars)

    r = 1
    c = 1

    while r * c < len(chars):
        if (c < r) or (c - r > 1):
            c += 1
            continue
        r += 1
    return r, c


print(rectangle(chars))

# chars = "imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau"

# for cols in range(9):
#     for row in range(cols):
#         if cols * row >= len(chars):
#             if cols > row:
#                 if cols - row <= 1:
#                     print(cols, row)
