from prices import get_max_profit


def test_max_profit():
    assert get_max_profit([1, 5, 3, 2]) == 4
    assert get_max_profit([7, 2, 8, 9]) == 7
    assert get_max_profit([1, 6, 7, 9]) == 8
    assert get_max_profit([9, 7, 4, 1]) == -2
    assert get_max_profit([1, 1, 1, 1]) == 0
