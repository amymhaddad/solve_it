from intersection import intersect


def test_intersection():
    assert intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or [9, 4]
    assert intersect([], [9, 4, 9, 8, 4]) == []
    assert intersect([1, 2, 3], []) == []
    assert intersect([], []) == []
