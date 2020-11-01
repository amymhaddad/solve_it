"""
(1) Assume that we can calculate a word's "score" by
    adding the scores of each letter -- where a=1, b=2,
    c=3, and so forth (ignoring case).  Ask the user for
    a sentence, and then create a dict based on that
    sentence, in which the keys are the words and the
    values are the "scores" for the words.

    bad cab   # output will be {'bad':4, 'cab':6} 

    ord('a') # 97 == ASCII value

(2) Repeat (1), but ignore in the dict output any
    word that has < 3 letters or > 7 letters.

(3) Flip a dict, so the keys become values and vice versa.

    {'a':1, 'b':2, 'c':3} ==> {1:'a', 2:'b', 3:'c'}

(4) Create a set comprehension from words.txt (the Linux
    dictionary).

    Use that set comprehension to create a dict (using
    a dict comprehension).  Ask the user to enter
    a sentence.  The output dict will be the user's words,
    and the values will be True/False, indicating if the
    word is in the dictionary.

    This is a floople test  => {'This':True,
                    'is':True, 'a':True, 'floople':False,
		    'test':True}
"""

# Exercise 1 and 2
from string import ascii_lowercase as letters

words = "this is a bunch of words"


def word_count(word):
    return sum([ord(letter) - 96 for letter in word.lower()])


scores = {
    word: word_count(word)
    for word in words.split()
    if len(word) >= 3 and len(word) <= 7
}


# Exercise 3:
flip = {letter: i for i, letter in enumerate(letters, 1)}

flop = {num: letter for letter, num in flip.items()}


# Exercise 4:
sent = "This is a flopple test".split()

set_comp = {word for word in open("wcfile.txt").read().split()}

result = {word: word in set_comp for word in sent}
