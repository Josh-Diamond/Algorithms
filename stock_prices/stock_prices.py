#!/usr/bin/python

import argparse

def find_max_profit(list):
    biggest_price = 0
    for price in range(0, len(list)):
        if list[price] > list[biggest_price]:
            biggest_price = price
    buyers_list = list[0: biggest_price]
    smallest_price = 0
    for buy_price in range(0, len(buyers_list)):
        if buyers_list[buy_price] < buyers_list[smallest_price]:
            smallest_price = buy_price
    return list[biggest_price] - buyers_list[smallest_price]

print(find_max_profit([1050, 270, 1540, 3800, 2]))

# ///////////////////////////
# Alternate Solution:

# def find_max_profit(prices):
#   highest_price = max(prices)
#   new_list = prices[0:prices.index(highest_price)]
#   lowest_before = min(new_list)
#   return highest_price - lowest_before
# print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#     args = parser.parse_args()
#
#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))

