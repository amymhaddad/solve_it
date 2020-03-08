from majority import majority_element_approach_1, majority_element_approach_2


def test_majority():
    assert majority_element_approach_1([3, 2, 3]) == 3
    assert majority_element_approach_2([3, 2, 3]) == 3
