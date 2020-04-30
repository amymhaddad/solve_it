"""
Write a function reverse_words() that takes a message as a messageof characters and reverses the order of the messagein place. ↴

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
"""


# Approach 1
def reverse_words(message):
    message_len = len(message)

    swap_letters(message, message_len - 1, 0)

    right = 0
    for left in range(message_len + 1):
        if left == message_len or message[left] == " ":
            swap_letters(message, left - 1, right)
            right = left + 1
    return message


def swap_letters(message, left, right):

    while right < left:
        message[left], message[right] = message[right], message[left]
        left -= 1
        right += 1
    return message


# Approach 2
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
