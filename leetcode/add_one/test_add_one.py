from add_one import add_one_to_list


def test_add_one_to_list():
    assert add_one_to_list([1, 2, 3]) == [1, 2, 4]
    assert add_one_to_list([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert add_one_to_list([9]) == [1, 0]
    assert add_one_to_list([1, 0]) == [1, 1]
    assert add_one_to_list([9, 9]) == [1, 0, 0]
