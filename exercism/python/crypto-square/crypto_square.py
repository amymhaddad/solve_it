import re

# value = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
value = "This is fun"


def normalize_string(plain_text):

    return "".join(
        [char.lower() for char in plain_text if char.isalpha() or char.isdigit()]
    )


chars = normalize_string(value)


# def create_rectangle(chars):
#     row = 0
#     col = 1


#     # I need to have some condintion to get the cols and rows to stop incrementing
#     while True:


# print(create_rectangle(chars))


c = 1

total = 9

"""
col 1 has 2 possible row pairs: (0, 1)
col 2 has 2 possbile row pairs: (1, 2)

c r
1 0
1 1
2 1
2 2
3 2
3 3
4 3
4 4

-First I create "row" numbers that could satisfy the 2 conditions
-Then I sub those numbers into the cond to see what works
# # For each value in the outer for loop i need to do 2 things: see if c >= r and c-r <= 1

# IF i put "row" on the outside of the loop, then it gets updated on each iteration of loop.
# BUT if I put it on the inside, then it only gets updated on after the completion of each loop

#col is continuously updated -- which is what I want it to do. BUT row is reset each time -- after the completion of each inner loop.
 
"""


def rect(c):

    col = 1
    while col < 9:
        row = col - 1
        for num in range(2):
            if (row * col >= 54) and (col >= row and col - row <= 1):
                return col, row
            else:
                row += 1
            print(col, row)
        col += 1


print(rect(c))

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

