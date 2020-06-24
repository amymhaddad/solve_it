from permutation import (
    is_permutation_approach_1,
    is_permutation_approach_2,
    is_permutation_approach_3,
)


def test_is_permutation():
    assert is_permutation_approach_1("cat", "tac") == True
    assert is_permutation_approach_1("", "dog") == False
    assert is_permutation_approach_2("cat", "tac") == True
    assert is_permutation_approach_2("", "dog") == False
    assert is_permutation_approach_3("cat", "tac") == True
    assert is_permutation_approach_3("", "dog") == False
