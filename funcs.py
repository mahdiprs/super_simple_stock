"""
This file contains all relevant functions for the calculation
"""


# function to calculate the dividend yield
# create class stock
class Stock(object):
    def __init__(self, stock_symbol, stock_type,  last_dividend, fixed_dividend, par_value):
        # type: (str, str, double, double, double) -> object
        self.stock_symbol = stock_symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

stock_list = []

stock_list.append(Stock("TEA", "Common", 0, 0, 100))
stock_list.append(Stock("POP", "Common", 8, 0, 100))
stock_list.append(Stock("ALE", "Common", 23, 0, 60))
stock_list.append(Stock("GIN", "Preferred", 8, 2, 100))
stock_list.append(Stock("JOE", "Common", 13, 0, 250))

for item in stock_list:
    print item.stock_symbol



