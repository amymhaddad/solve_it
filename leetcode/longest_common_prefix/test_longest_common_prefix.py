from longest_common_prefix import prefix


def test_prefix():
    assert prefix([]) == ""
    assert prefix(["a", "a"]) == "a"
    assert prefix(["aa", "aa"]) == "aa"
    assert prefix(["dog", "racecar", "car"]) == ""
    assert prefix(["flower", "flow", "flight"]) == "fl"
