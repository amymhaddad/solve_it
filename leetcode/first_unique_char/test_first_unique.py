from first_unique import unique_approach_1, unique_approach_2


def test_unique_letter():
    assert unique_approach_1("loveleetcode") == 2
    assert unique_approach_1("leetcode") == 0
    assert unique_approach_1("aaa") == -1
    assert unique_approach_1("") == -1
    assert unique_approach_1("x") == 0

    assert unique_approach_2("loveleetcode") == 2
    assert unique_approach_2("leetcode") == 0
    assert unique_approach_2("aaa") == -1
    assert unique_approach_2("") == -1
    assert unique_approach_2("x") == 0
