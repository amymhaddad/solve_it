from stones_jewels import count_jewels


def test_three_jewels():
    assert count_jewels("aA", "aAAbbb") == 3


def test_zero_jewels():
    assert count_jewels("z", "Z") == 0
