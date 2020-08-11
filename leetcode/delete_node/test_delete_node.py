from delete_node import deleteNode


def test_delete_node():
    assert deleteNode([4, 5, 1, 9], 5) == [4, 1, 9]

