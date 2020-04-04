from reverse import reverse_words


def test_one_word():
    message = list("vault")
    expected = list("vault")
    assert reverse_words(message) == expected


def test_two_words():
    message = list("thief cake")
    expected = list("cake thief")
    assert reverse_words(message) == expected


def test_three_words():
    message = list("one another get")
    expected = list("get another one")
    assert reverse_words(message) == expected


def test_multiple_words_same_length():
    message = list("rat the ate cat the")
    expected = list("the cat ate the rat")
    assert reverse_words(message) == expected


def test_multiple_words_different_lengths():
    message = list("yummy is cake bundt chocolate")
    expected = list("chocolate bundt cake is yummy")
    assert reverse_words(message) == expected


def test_empty_string():
    message = list("")
    expected = list("")
    assert reverse_words(message) == expected
