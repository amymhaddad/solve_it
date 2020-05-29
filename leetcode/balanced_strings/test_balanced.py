from balanced import balanced_strings


def test_balanced_strings():
    assert balanced_strings("RLRRLLRLRL") == 4
    assert balanced_strings("RLLLLRRRLR") == 3
    assert balanced_strings("LLLLRRRR") == 1
    assert balanced_strings("RLRRRLLRLL") == 2
    assert balanced_strings("R") == 0
    assert balanced_strings("RLR") == 0
