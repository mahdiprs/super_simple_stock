"""

This file contains all relevant functions and classes for the Super Simple Stock Market assignment

@Author: Mahdi Parsa
"""

import time
import math


# create class stock
class Stock(object):
    all_trades = list()  # a list to keep track of all trades

    def __init__(self, stock_symbol, stock_type, last_dividend, fixed_dividend, par_value, stock_price=0):
        # type: (str, str, int, float, int, float) -> Stock

        self.stock_symbol = stock_symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.stock_price = stock_price

    (" a method for validating the stock symbol.\n"
     "    Symbols are {\"TEA\", \"POP\", \"ALE\", \"GIN\", \"JOE\"} ")

    @property
    def stock_symbol(self):
        return self._stock_symbol

    @stock_symbol.setter
    def stock_symbol(self, value):
        if value.upper() not in {"TEA", "POP", "ALE", "GIN", "JOE"}:
            raise TypeError('It is not a valid stock label.')
        self._stock_symbol = value

    (" A method for validating the stock types. Types are either \n"
     "    {\"COMMON\", \"PREFERRED\"}")

    @property
    def stock_type(self):
        return self._stock_type

    @stock_type.setter
    def stock_type(self, value):
        if value.upper() not in {"COMMON", "PREFERRED"}:
            raise TypeError('It is not a valid stock type.')
        self._stock_type = value

    def dividend_yield(self, price):
        """ Given a price for a stock it calculates the Dividend Yield """

        if self.stock_type.upper() == "COMMON":
            dividend_yield_value = self.last_dividend / price
        else:
            dividend_yield_value = self.fixed_dividend * self.par_value * 0.01 / price
        return dividend_yield_value

    def calculate_pe_ratio(self, price):
        """ Given a price for a stock it calculates P/E ratio """

        dividend = self.dividend_yield(price)
        if dividend > 0:
            ratio = price / dividend
            return ratio
        else:
            return "The P/E ratio is not defined for stock %s since dividend yield is zero. " % self.stock_symbol

    def record_trade(self, quantity_of_share, trade_indicator, trade_price):
        # type: (float, string, float) -> Stock

        """ Record a trade for a given stock with quantity of share, trade indicator, trade price.
        the trade indicator is either buy or sell """

        trade_time = time.time()  # current time
        trade = Trade(self.stock_symbol, trade_time, quantity_of_share, trade_indicator, trade_price)
        if trade:
            self.all_trades.append(trade)
            print ("Adding a new trade was successful.")
            return True
        else:
            print ("Adding a new trade was not successful.")
            return False

    @property
    def calculate_volume_stock_price(self):
        """ Given a stock it calculates volume stock price for based on trade in past 15 minuets """
        trade_price_times_quantity = 0
        sum_quantity = 0
        current_time = time.time()
        if not self.all_trades:
            print "No trades have been recorded."
        else:
            for a_trade in self.all_trades:
                if current_time <= a_trade.trade_time + 15 * 60:
                    trade_price_times_quantity += a_trade.quantity_of_share * a_trade.trade_price
                    sum_quantity += a_trade.quantity_of_share
            if sum_quantity == 0:
                print "Quantity of shares were zero when stock recorded."
            else:
                return float(trade_price_times_quantity) / float(sum_quantity)

    @property
    def stock_last_trade_price(self):
        """ Find the latest trade recorded and the latest price for a given stock"""
        latest_trade_time = 0
        latest_trade_price = 0
        for a_trade in self.all_trades:
            if a_trade.trade_time >= latest_trade_time:
                latest_trade_time = a_trade.trade_time
                latest_trade_price = a_trade.trade_price
        return latest_trade_price


class Trade(object):
    def __init__(self, stock_symbol, trade_time, quantity_of_share, trade_indicator, trade_price):
        # type: (str, time, int, str, float) -> Trade
        self.stock_symbol = stock_symbol
        self.trade_time = trade_time
        self.quantity_of_share = quantity_of_share
        self.trade_indicator = trade_indicator
        self.trade_price = trade_price

    (" A method for validating a trade indicator. These indicators are \n"
     "    {\"BUY\", \"SELL\"} ")

    @property
    def trade_indicator(self):
        return self._trade_indicator

    @trade_indicator.setter
    def trade_indicator(self, value):
        if value.upper() not in {"BUY", "SELL"}:
            raise TypeError('It is not a valid trade label.')
        self._trade_indicator = value


def geometric_mean(stock_prices):
    """ Calculates the geometric means of a list of numbers"""
    product = 1
    for item in stock_prices:
        product = float(product) * float(item)
    number_of_items = len(stock_prices)
    return math.pow(product, 1 / float(number_of_items))


def calculate_gbce(stocks):
    """ Calculate t the gbce all share index"""
    volume_stock_price = []
    for item in stocks:
        volume_stock_price.append(item.stock_last_trade_price)
    return geometric_mean(volume_stock_price)