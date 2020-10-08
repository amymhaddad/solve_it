from adjacent_duplicates import remove_duplicates


def test_remove_duplicates_in_middle():
    assert (remove_duplicates("abbaca")) == "ca"


def test_remove_duplicates_at_start():
    assert (remove_duplicates("aacd")) == "cd"


def test_remove_duplicates_at_end():
    assert (remove_duplicates("cdaa")) == "cd"


def test_remove_duplicates_at_start_and_end():
    assert (remove_duplicates("aaqbb")) == "q"
