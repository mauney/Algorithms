#!/usr/bin/python

import argparse

def find_max_profit(prices):
    if len(prices) < 2:
        return "No profit possible without at least two prices as input."
    # set initial value for profit
    profit = prices[1] - prices[0]
    # for each price other than the last
    for i, buy_price in enumerate(prices[:-1]):
        # get the highest possible future sale price
        max_sale = max(prices[i + 1:])
        # compare the profit to the saved profit and keep highest
        profit = max(profit, max_sale - buy_price)
    # return the maximum possible profit
    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))