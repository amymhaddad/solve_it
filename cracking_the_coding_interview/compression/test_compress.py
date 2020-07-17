from string_compression import compress


def test_compressed_string():
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("aabbcc") == "aabbcc"
    assert compress("aabcc") == "aabcc"
