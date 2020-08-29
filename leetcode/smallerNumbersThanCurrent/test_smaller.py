from smaller import get_smallest


def test_get_smallest():
    assert get_smallest([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert get_smallest([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    assert get_smallest([7, 7, 7, 7]) == [0, 0, 0, 0]
