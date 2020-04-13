from baseball_game import calPoints


def test_score():
    assert calPoints(["5", "2", "C", "D", "+"]) == 30
    assert calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
