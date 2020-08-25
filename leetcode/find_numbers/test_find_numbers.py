from find_numbers import findnumbers


def test_findnumbers():
    assert findnumbers([12, 345, 2, 6, 7896]) == 2
    assert findnumbers([555, 901, 482, 1771]) == 1
