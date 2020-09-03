from string import ascii_lowercase as lower

MORSE_CODE_REPRESENTATIONS = [
    [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
]


def unique_morse_code_representations(words):

    letters_to_morse_code = {
        letter: morse_code
        for chars in MORSE_CODE_REPRESENTATIONS
        for letter, morse_code in zip(lower, chars)
    }
    return letters_to_morse_code


print(unique_morse_code_representations(["gin", "zen", "gig", "msg"]))


# for chars in MORSE_CODE_REPRESENTATIONS:
#     for letter, morse_code in zip(lower, chars):
#         print(letter, morse_code)
