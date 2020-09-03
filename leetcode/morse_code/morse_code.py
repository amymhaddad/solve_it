from string import ascii_lowercase as lower

MORSE_CODE_REPRESENTATIONS = [
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


def unique_morse_code_representations(words):

    letter_to_morse_code = {
        letter: morse_code
        for letter, morse_code in zip(list(lower), MORSE_CODE_REPRESENTATIONS)
    }
    seen = {"".join(letter_to_morse_code[letter] for letter in word) for word in words}

    return len(seen)


print(unique_morse_code_representations(["gin", "zen", "gig", "msg"]))
