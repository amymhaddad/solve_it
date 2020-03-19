<<<<<<< HEAD
from stocks import stock_prices


def test_stock_prices():
    assert stock_prices([7, 1, 5, 3, 6, 4]) == 7
    assert stock_prices([1, 2, 3, 4, 5]) == 4
    assert stock_prices([5, 4, 3, 2, 1]) == 0
    assert stock_prices([2, 2, 5]) == 3
    assert stock_prices([4, 1, 2]) == 1
    assert stock_prices([2, 1, 2, 0, 1]) == 2
=======

from stocks import stock_prices

def test_stock_prices():
    assert stock_prices([7,1,5,3,6,4]) == 7
>>>>>>> 895eb1d... First iteration of algorithm
