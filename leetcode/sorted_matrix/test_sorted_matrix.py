from sorted_matrix import get_negative_numbers


def test_negative_nums():
    assert get_negative_numbers([[10]]) == 0
    assert (
        get_negative_numbers(
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        )
        == 8
    )
    assert get_negative_numbers([[3, 2], [1, 0]]) == 0
    assert get_negative_numbers([[1, -1], [-1, -1]]) == 3
    assert get_negative_numbers([[-1]]) == 1
    assert (
        get_negative_numbers(
            [
                [3, -1, -3, -3, -3],
                [2, -2, -3, -3, -3],
                [1, -2, -3, -3, -3],
                [0, -3, -3, -3, -3],
            ]
        )
        == 16
    )
