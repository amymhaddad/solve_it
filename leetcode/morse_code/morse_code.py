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

    letter_to_morse_code = {
        letter: morse_code
        for letters in MORSE_CODE_REPRESENTATIONS
        for letter, morse_code in zip(lower, letters)
    }

    unique_transformations = set()
    each_transformation = ""

    for word in words:
        for letter in word:
            each_transformation += letter_to_morse_code[letter]
        unique_transformations.add(each_transformation)
        each_transformation = ""

    return len(unique_transformations)


print(unique_morse_code_representations(["gin", "zen", "gig", "msg"]))
