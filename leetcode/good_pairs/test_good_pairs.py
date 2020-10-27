from good_pairs import goodPairs


def test_good_pairs():
    assert goodPairs([1, 1, 1, 1]) == 6
    assert goodPairs([1, 2, 3, 1, 1, 3]) == 4
    assert goodPairs([1, 2, 3]) == 0
