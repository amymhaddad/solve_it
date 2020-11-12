from subarrays import sum_odd_length_subarrays


def test_array_long_odd_length_array():
    arr = [1, 4, 2, 5, 3]
    assert sum_odd_length_subarrays(arr) == 58


def test_short_odd_length_array():
    arr = [10, 11, 12]
    assert sum_odd_length_subarrays(arr) == 66


def test_single_number_odd_length_array():
    arr = [1]
    assert sum_odd_length_subarrays(arr) == 1


def test_short_even_array_length():
    arr = [1, 2]
    assert sum_odd_length_subarrays(arr) == 3


def test_long_even_array_length():
    arr = [6, 9, 14, 5, 3, 8, 7, 12, 13, 1]
    assert sum_odd_length_subarrays(arr) == 878
