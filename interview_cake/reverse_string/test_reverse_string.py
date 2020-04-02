from reverse_string import reverse


def test_empty_string():
    assert reverse([]) == []


def test_single_character_string():
    assert reverse(["A"]) == ["A"]


def test_longer_string():
    assert reverse(["A", "B", "C", "D", "E"]) == ["E", "D", "C", "B", "A"]
