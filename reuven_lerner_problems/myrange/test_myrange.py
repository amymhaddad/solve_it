from myrange import myrange


def test_only_stop_value():
    assert myrange(5) == [0, 1, 2, 3, 4]


def test_stop_start_values():
    assert myrange(5, 10) == [5, 6, 7, 8, 9]


def test_stop_start_interval_values():
    assert myrange(5, 20, 3) == [5, 8, 11, 14, 17]
