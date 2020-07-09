from urlify import add_characters_to_string


def test_add_characters_to_string():
    assert add_characters_to_string("Mr. John Smith    ", 13) == "Mr%20John%20Smith"
