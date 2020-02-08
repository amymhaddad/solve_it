from pivot import find_pivot


def test_find_pivot():
    assert find_pivot([1, 7, 3, 6, 5, 6]) == 3
    assert find_pivot([1, 2, 3]) == -1
    assert find_pivot([-1, -1, -1, 0, 1, 1]) == 0
    assert find_pivot([-1, -1, 0, 1, 1, 0]) == 5
