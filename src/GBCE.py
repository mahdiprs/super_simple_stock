"""

This file contains all relevant functions for calculation GBCE
__author__ = "Mahdi Parsa"
"""


def geometric_mean(stock_prices):
    """ Calculates the geometric means of a list of numbers"""
    try:
        product = 1.0
        for item in stock_prices:
            product = float(product) * float(item)
        number_of_items = len(stock_prices)
        return product ** (1.0 / float(number_of_items))
    except:
        raise TypeError("The stocks prices list is empty.")


def calculate_gbce(stocks):
    """ Calculate the gbce all share index"""
    try:
        volume_stock_price = []
        for item in stocks:
            volume_stock_price.append(item.stock_last_trade_price)
        return geometric_mean(volume_stock_price)
    except:
        raise TypeError("The stocks list is empty.")
