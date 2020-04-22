from word_cloud import word_cloud_data


def test_simple_sentence():
    input = "I like cake"
    assert word_cloud_data(input) == {"i": 1, "like": 1, "cake": 1}


def test_longer_sentence():
    input = "Chocolate cake for dinner and pound cake for dessert"
    assert word_cloud_data(input) == {
        "and": 1,
        "pound": 1,
        "for": 2,
        "dessert": 1,
        "chocolate": 1,
        "dinner": 1,
        "cake": 2,
    }


def test_punctuation():
    input = "Strawberry short cake? Yum!"
    assert word_cloud_data(input) == {"cake": 1, "strawberry": 1, "short": 1, "yum": 1}


def test_hyphenated_words():
    input = "Dessert - mille-feuille cake"
    assert word_cloud_data(input) == {"cake": 1, "dessert": 1, "mille-feuille": 1}


def test_ellipses_between_words():
    input = "Mmm...mmm...decisions...decisions"
    assert word_cloud_data(input) == {"mmm": 2, "decisions": 2}


def test_apostrophes():
    input = "Allie's Bakery: Sasha's Cakes"
    assert word_cloud_data(input) == {
        "bakery": 1,
        "cakes": 1,
        "allie's": 1,
        "sasha's": 1,
    }
