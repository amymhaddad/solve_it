from permutation_palindrome import (
    has_palindrome_permutation_approach_1,
    has_palindrome_permutation_approach_2,
    has_palindrome_permutation_approach_3,
    has_palindrome_permutation_approach_4,
)


def test_is_palindrome_approach_1():
    assert has_palindrome_permutation_approach_1("aabcbcd") == True
    assert has_palindrome_permutation_approach_1("aabccbdd") == True
    assert has_palindrome_permutation_approach_1("aabcd") == False
    assert has_palindrome_permutation_approach_1("aabbcd") == False
    assert has_palindrome_permutation_approach_1("") == True
    assert has_palindrome_permutation_approach_1("a") == True


def test_is_palindrome_approach_2():
    assert has_palindrome_permutation_approach_2("aabcbcd") == True
    assert has_palindrome_permutation_approach_2("aabccbdd") == True
    assert has_palindrome_permutation_approach_2("aabcd") == False
    assert has_palindrome_permutation_approach_2("aabbcd") == False
    assert has_palindrome_permutation_approach_2("") == True
    assert has_palindrome_permutation_approach_2("a") == True


def test_is_palindrome_approach_():
    assert has_palindrome_permutation_approach_3("aabcbcd") == True
    assert has_palindrome_permutation_approach_3("aabccbdd") == True
    assert has_palindrome_permutation_approach_3("aabcd") == False
    assert has_palindrome_permutation_approach_3("aabbcd") == False
    assert has_palindrome_permutation_approach_3("") == True
    assert has_palindrome_permutation_approach_3("a") == True


def test_is_palindrome_approach_4():
    assert has_palindrome_permutation_approach_4("aabcbcd") == True
    assert has_palindrome_permutation_approach_4("aabccbdd") == True
    assert has_palindrome_permutation_approach_4("aabcd") == False
    assert has_palindrome_permutation_approach_4("aabbcd") == False
    assert has_palindrome_permutation_approach_4("") == True
    assert has_palindrome_permutation_approach_4("a") == True
