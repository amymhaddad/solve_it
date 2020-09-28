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


chars = "thisisfun"


def create_rectangle(chars):
    normalized_string_length = len(chars)

    r = 1
    c = 1

    while r * c < len(chars):
        if (c < r) or (c - r > 1):
            c += 1
            continue
        r += 1
    return {"row": r, "column": c}


rectangle = create_rectangle(chars)


def parse_rectangle(rectangle):

    each_row = []
    start = 0
    end = rectangle["column"]

    while end <= len(chars):
        for letter in chars[start:end]:
            each_row.append(letter + ",")
        each_row.append("\n")
        start = end
        end += rectangle["column"]

    return "".join(each_row)


# ['t,', 'h,', 'i,', '\n', 's,', 'i,', 's,', '\n', 'f,', 'u,', 'n,', '\n']

# Iterate through the string; spilit on \n 
#Use zip to grab each col 
parsed_rectangle = parse_rectangle(rectangle)


# each_row = [[chars] for rows in parsed_rectangle.split("\n") for chars in rows]

print(parsed_rectangle)
