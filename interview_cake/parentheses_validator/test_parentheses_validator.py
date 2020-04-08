from parentheses_validator import multi_parens_approach_1, multi_parens_approach_2


# def test_multi_parens_approach_1():
#     assert multi_parens_approach_1("()") == True
#     assert multi_parens_approach_1("([]{[]})[]{{}()}") == True
#     assert multi_parens_approach_1("([)]") == False
#     assert multi_parens_approach_1("([][]}") == False
#     assert multi_parens_approach_1("[[]()") == False
#     assert multi_parens_approach_1("[[]]())") == False
#     assert multi_parens_approach_1("") == True


def test_multi_parens_approach_2():
    assert multi_parens_approach_2("()") == True

    assert multi_parens_approach_2("([]{[]})[]{{}()}") == True

    assert multi_parens_approach_2("([)]") == False

    assert multi_parens_approach_2("([][]}") == False

    assert multi_parens_approach_2("[[]()") == False
    assert multi_parens_approach_2("[[]()") == False
    assert multi_parens_approach_2("[[]()") == False
