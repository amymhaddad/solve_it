from inflight_entertainment import (
    can_two_movies_fill_flight_approach_1,
    can_two_movies_fill_flight_approach_2,
)


def test_can_two_movies_fill_flight_approach_1():
    assert can_two_movies_fill_flight_approach_1([2, 4], 1) == False
    assert can_two_movies_fill_flight_approach_1([2, 4], 6) == True
    assert can_two_movies_fill_flight_approach_1([3, 8], 6) == False
    assert can_two_movies_fill_flight_approach_1([3, 8, 3], 6) == True
    assert can_two_movies_fill_flight_approach_1([1, 2, 3, 4, 5, 6], 7) == True
    assert can_two_movies_fill_flight_approach_1([4, 3, 2], 5) == True
    assert can_two_movies_fill_flight_approach_1([6], 6) == False
    assert can_two_movies_fill_flight_approach_1([], 2) == False


def test_can_two_movies_fill_flight_approach_2():
    assert can_two_movies_fill_flight_approach_2([2, 4], 1) == False
    assert can_two_movies_fill_flight_approach_2([2, 4], 6) == True
    assert can_two_movies_fill_flight_approach_2([3, 8], 6) == False
    assert can_two_movies_fill_flight_approach_2([3, 8, 3], 6) == True
    assert can_two_movies_fill_flight_approach_2([1, 2, 3, 4, 5, 6], 7) == True
    assert can_two_movies_fill_flight_approach_2([4, 3, 2], 5) == True
    assert can_two_movies_fill_flight_approach_2([6], 6) == False
    assert can_two_movies_fill_flight_approach_2([], 2) == False
