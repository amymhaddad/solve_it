from palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("daily") == False
