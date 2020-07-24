from peak import peak_mountain


def test_peak_index():
    assert peak_mountain([0, 1, 0]) == 1
    assert peak_mountain([0, 2, 1, 0]) == 1
    assert peak_mountain([3, 4, 5, 1]) == 2
    # assert peak_mountain([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]) == 2
