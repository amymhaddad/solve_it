from contains_duplicate import has_duplicates_approach_1, has_duplicates_approach_2


def test_duplicates():
    assert has_duplicates_approach_1([1, 2, 3, 1]) == True
    assert has_duplicates_approach_1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert has_duplicates_approach_1([1, 2, 3, 4]) == False

    assert has_duplicates_approach_2([1, 2, 3, 1]) == True
    assert has_duplicates_approach_2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert has_duplicates_approach_2([1, 2, 3, 4]) == False
