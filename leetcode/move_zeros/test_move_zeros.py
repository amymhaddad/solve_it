from move_zeros import move_zero_numbers


def test_move_zero_numbers():
    assert move_zero_numbers([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zero_numbers([1, 0, 1]) == [1, 1, 0]
