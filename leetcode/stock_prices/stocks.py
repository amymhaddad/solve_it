def stock_prices(prices):

    totals = 0
    index = 0
    for i, price in enumerate(prices):

        next_day_price = prices[(i + 1) % len(prices)]
        profit = next_day_price - price

        if profit > 0:
            totals += profit
        index += 1

        if index == len(prices) - 1:
            break

    return totals
