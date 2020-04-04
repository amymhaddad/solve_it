"""
Write a function reverse_words() that takes a message as a messageof characters and reverses the order of the messagein place. ↴

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
"""


def reverse_words(message):

    if " " not in message:
        return message

    left = len(message) - 1
    right = 0

    while right < left:
        message[left], message[right] = message[right], message[left]
        left -= 1
        right += 1

    right = 0
    space = message.index(" ")
    left = space - 1

    for letter in message:
        if letter.isalpha() and right < left:
            message[right], message[left] = message[left], message[right]
            left -= 1
            right += 1

        elif letter.isspace():
            right = space + 1
            try:
                space = message.index(" ", right + 1)
                left = space - 1
            except ValueError:
                space = len(message)
                left = space - 1

    return message
