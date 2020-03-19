from str import (
    find_index_approach_a, 
    find_index_approach_b
)

def test_needle_in_haystack():
    assert find_index_approach_a("hello", "ll") == 2
    assert find_index_approach_a("aaaaa", "bba") == -1
    assert find_index_approach_a("hi", "") == 0

    assert find_index_approach_b("hello", "ll") == 2
    assert find_index_approach_b("aaaaa", "bba") == -1
    assert find_index_approach_b("hi", "") == 0