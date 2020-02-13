from remove import remove_duplicate


def test_remove_duplicate():
    assert remove_duplicate([1, 1, 2]) == 2
