from v2_shuffle import shuffle


def test_shuffle_array():
    assert shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
    assert shuffle([7, 5, 9, 7, 5, 8, 10, 4, 3, 3, 2, 5, 9, 10], 7) == [
        7,
        4,
        5,
        3,
        9,
        3,
        7,
        2,
        5,
        5,
        8,
        9,
        10,
        10,
    ]
    # assert shuffle([], 0 == [])
