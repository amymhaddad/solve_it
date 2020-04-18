"""
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. 
"""


def has_palindrome_permutation_approach_1(word):
    start = 0
    end = len(word) - 1

    if end <= 1:
        return True

    while start < end:
        if word[start] == word[end]:
            if end - start == 1:
                return False
            return True
        else:
            start += 1
            end -= 1
    return False


def has_palindrome_permutation_approach_2(word):

    letter_counter = {}

    counter = 0
    num_comparison = 0

    for i, letter in enumerate(word):
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    for number in letter_counter.values():
        if number > 1:
            if num_comparison == 0:
                num_comparison = number
                counter += 1
                continue
            if number == num_comparison:
                counter += 1

    if len(word) // 2 == counter:
        return True

    if counter > 1 and counter % 2 != 0:
        return True
    return False


def has_palindrome_permutation_approach_3(word):
    letter_counter = {}

    even = 0
    odd = 0

    for i, letter in enumerate(word):
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    for number in letter_counter.values():
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd <= 1


def has_palindrome_permutation_approach_4(word):
    letter_counter = {}

    letters_with_odd_counts = set()

    for i, letter in enumerate(word):
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    for letter, count in letter_counter.items():

        if count == 1:
            letters_with_odd_counts.add(letter)

    if len(letters_with_odd_counts) > 1 and len(word) > 1:
        return False
    return True
