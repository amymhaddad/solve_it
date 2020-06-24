from is_unique import is_unique_approach_1, is_unique_approach_2, is_unique_approach_3


def test_is_unique():
    assert is_unique_approach_1("abc") == True
    assert is_unique_approach_1("aabc") == False
    assert is_unique_approach_1("") == True


def test_is_unique():
    assert is_unique_approach_2("abc") == True
    assert is_unique_approach_2("aabc") == False
    assert is_unique_approach_2("") == True


def test_is_unique():
    assert is_unique_approach_3("abc") == True
    assert is_unique_approach_3("aabc") == False
    assert is_unique_approach_3("") == True
