"""

This file contains all relevant functions and classes for the Super Simple Stock Market assignment
__author__ = "Mahdi Parsa"
"""
import math


def geometric_mean(stock_prices):
    """ Calculates the geometric means of a list of numbers"""
    product = 1
    for item in stock_prices:
        product = float(product) * float(item)
    number_of_items = len(stock_prices)
    return math.pow(product, 1 / float(number_of_items))


def calculate_gbce(stocks):
    """ Calculate the gbce all share index"""
    volume_stock_price = []
    for item in stocks:
        volume_stock_price.append(item.stock_last_trade_price)
    return geometric_mean(volume_stock_price)
