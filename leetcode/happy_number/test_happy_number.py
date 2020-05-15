from happy_number import is_happy


def test_two_digit_number():
    assert is_happy(19) == True


def test_one_digit_number():
    assert is_happy(1) == True
