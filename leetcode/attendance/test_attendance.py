from attendance import check_record


def test_check_record():
    assert check_record("PPALLP") == True
    assert check_record("PPALLL") == False
    assert check_record("AAAA") == False
    assert check_record("AA") == False
