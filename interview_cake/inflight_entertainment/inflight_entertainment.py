"""
So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""


def can_two_movies_fill_flight_approach_1(movie_lengths, flight_length):
    if len(movie_lengths) <= 1:
        return False

    movies = {}

    for i, movie_length in enumerate(movie_lengths):
        difference = flight_length - movie_length

        if difference in movie_lengths:
            movies[i] = movie_length

    return len(movies) >= 2


def can_two_movies_fill_flight_approach_2(movie_lengths, flight_length):
    if len(movie_lengths) <= 1:
        return False

    movies_seen = set()
    for movie_length in movie_lengths:
        difference = flight_length - movie_length

        if difference in movie_lengths:
            if movie_length not in movies_seen:
                movies_seen.add(movie_length)
            else:
                return True
    return len(movies_seen) >= 2
