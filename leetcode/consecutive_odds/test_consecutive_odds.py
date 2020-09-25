from consecutive_odds import three_consecutive_odds


def test_one_odd_number():
    assert three_consecutive_odds([2, 6, 4, 1]) == False


def test_two_odd_numbers():
    assert three_consecutive_odds([2, 6, 1, 1]) == False


def test_three_odd_numbers():
    assert three_consecutive_odds([1, 6, 1, 1]) == False


def test_three_consecutive_odd_numbers_at_end():
    assert three_consecutive_odds([2, 1, 1, 1]) == True


def test_three_consecutive_odd_numbers_in_middle():
    assert three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
