"""
Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
"""


def get_max_profit_2(prices):
    if not prices:
        return 0

    min_price_so_far = prices[0]
    max_profit = prices[1] - prices[0]

    for i, current_price in enumerate(prices[1:]):
        current_profit = current_price - min_price_so_far

        if current_price < min_price_so_far:
            min_price_so_far = current_price

        if max_profit < current_profit:
            max_profit = current_profit

    return max_profit
