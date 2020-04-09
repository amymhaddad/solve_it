import pytest

from paren_position import find_position


def test_all_openers_then_closers():
    assert find_position("((((()))))", 2) == 7


def test_mixed_openers_and_closers():
    assert find_position("()()((()()))", 5) == 10
