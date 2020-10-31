def is_armstrong_number(number):

    given_number = number
    total = 0
    total_digits = len(list(map(int, str(given_number))))

    while given_number > 0:

        total += (given_number % 10) ** total_digits
        given_number //= 10

    return number == total
