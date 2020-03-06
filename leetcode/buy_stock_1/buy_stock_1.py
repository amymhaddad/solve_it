"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

def max_profit(prices):

    if not len(prices):
        return 0

    minimum_price = prices[0]

    max_profit_so_far = 0

    for _, current_price in enumerate(prices, start=1):
        current_profit = current_price - minimum_price
        if current_price < minimum_price:
            minimum_price = current_price

        if current_profit > max_profit_so_far:
            max_profit_so_far = current_profit
    return max_profit_so_far
