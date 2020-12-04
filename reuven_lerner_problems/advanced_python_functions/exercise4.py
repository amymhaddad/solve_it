"""
(1) Write a function (make_pw_function) that takes a string of characters.
    It'll return a function that takes an integer as input.  When the
    returned function is invoked, it returns a string composed of randomly
    selected characters from the string, of the selected length.

    For example:

    alpha_pw_maker = make_pw_function('abcde')
    symbol_pw_maker = make_pw_function('!@#$%')

    print(alpha_pw_maker(5))  # returns 5-character password
    print(alpha_pw_maker(10))  # returns 10-character password

    print(symbol_pw_maker(5))  # returns 5-character password
    print(symbol_pw_maker(10))  # returns 10-character password
"""

import random


def make_pw_function(chars):
    def make_pw(number):
        output = ""
        for i in range(number):
            output += random.choice(chars)
        return output

    return make_pw


alpha_pw_maker = make_pw_function("abcde")
symbol_pw_maker = make_pw_function("!@#$%")

print(alpha_pw_maker(5))  # returns 5-character password
print(alpha_pw_maker(10))  # returns 10-character password

print(symbol_pw_maker(5))  # returns 5-character password
print(symbol_pw_maker(10))  # returns 10-character password}}
