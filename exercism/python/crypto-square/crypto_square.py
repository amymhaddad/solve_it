import re


def normalize_string(plain_text):

    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


# string = normalize_string(chars)


def create_rectangle(chars):
    # Test if perfect square
    factors = []
    start = 2
    char_length = len(chars)

    while char_length != 1:
        if char_length % start == 0:
            factors.append(start)
            result = char_length // start
            char_length = result
        else:
            start += 1

    if len(factors) == 2 and len(set(factors)) == 1:
        return {"row": factors[0], "column": factors[0]}

    # IF not perfect square:
    else:
        col = max(factors)
        row = col - 1
        while row * col < len(chars):
            if (col < row) or (col - row > 1):
                row += 1
                continue
            col += 1
        return {"row": row, "column": col}


# rectangle = create_rectangle("thisisfun")
# rectangle = create_rectangle("ifmanwasmeanttostayonthegroundgodwouldhavegivenusrootsff")
# print(rectangle)


def parse_rectangle(rectangle, chars):

    total_rows = []
    start = 0
    end = rectangle["column"]

    # while end < len(chars):
    while len(chars) - end > 1:
        each_row = chars[start:end]
        total_rows.append(each_row)
        start = end
        end += rectangle["column"]
        # import pdb

        # pdb.set_trace()
    total_rows.append(chars[start:])
    print(total_rows)

    #     each_row = []

    #     for letter in chars[start:end]:
    #         each_row.append(letter)
    #     total_rows.append(each_row)
    #     start = end
    #     end += rectangle["column"]
    #     if len(chars) - end == 1:
    #         total_rows.append(chars[start:])
    # print(total_rows)
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

# p [['t', 'h', 'i', 's'], ['i', 's', 'f', 'u']]
# ti  hs  if  su
