from largest import get_number_approach_1, get_number_approach_2, get_number_approach_3


def test_number_is_largest_and_twice_size():

    assert get_number_approach_1([3, 6, 1, 0]) == 1
    assert get_number_approach_1([1, 2, 3, 4]) == -1
    assert get_number_approach_1([0, 0, 0, 1]) == 3

    assert get_number_approach_2([3, 6, 1, 0]) == 1
    assert get_number_approach_2([1, 2, 3, 4]) == -1
    assert get_number_approach_2([0, 0, 0, 1]) == 3

    assert get_number_approach_3([3, 6, 1, 0]) == 1
    assert get_number_approach_3([1, 2, 3, 4]) == -1
    assert get_number_approach_3([0, 0, 0, 1]) == 3
