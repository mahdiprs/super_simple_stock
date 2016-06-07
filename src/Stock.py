""" A module to add stock and its properties"""

import time
from binary_search import get_index_binary_search
from Trade import Trade


# create class stock
class Stock(object):
    FIFTEEN_MINUTES = 15 * 60  # constant for retrieving recorded trades in past 15 minutes

    def __init__(self, stock_symbol, stock_type, last_dividend, fixed_dividend, par_value, stock_price=0):
        # type: (str, str, int, float, int, float) -> Stock
        """

        :type stock_symbol: float
        """
        self.stock_symbol = stock_symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.stock_price = stock_price
        self.all_trades = list()  # a list to keep track of all trades

    """ Validating stock symbols."""
    @property
    def stock_symbol(self):
        return self._stock_symbol

    @stock_symbol.setter
    def stock_symbol(self, value):
        if value.upper() not in {"TEA", "POP", "ALE", "GIN", "JOE"}:
            raise TypeError("Invalid stock label.")
        self._stock_symbol = value

    """"" Validating the stock types."""
    @property
    def stock_type(self):
        return self._stock_type

    @stock_type.setter
    def stock_type(self, value):
        if value.upper() not in {"COMMON", "PREFERRED"}:
            raise TypeError("It is not a valid stock type.")
        self._stock_type = value

    """ Validating last dividend type."""
    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError("Invalid last dividend type.")
        self._last_dividend = value

    """ Validating fixed dividend type."""
    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, value):
        if not isinstance(value, (int, long, float)) and not value:
            raise TypeError("Invalid fixed dividend type.")
        self._fixed_dividend = value

    """ Validating par value type."""
    @property
    def par_value(self):
        return self._par_value

    @par_value.setter
    def par_value(self, value):
        if not isinstance(value, (int, long)):
            raise TypeError("Invalid parameter value type.")
        self._par_value = value

    """ Validating stock price type."""
    @property
    def stock_price(self):
        return self._stock_price

    @stock_price.setter
    def stock_price(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError("Invalid price value type.")
        self._stock_price = value

    def dividend_yield(self, price):
        """ Given a price for a stock it calculates the Dividend Yield """

        if self.stock_type.upper() == "COMMON":
            return self.last_dividend / price
        else:
            return self.fixed_dividend * self.par_value * 0.01 / price

    def calculate_pe_ratio(self, price):
        """ Given a price for a stock it calculates P/E ratio """

        dividend = self.dividend_yield(price)
        if dividend > 0:
            ratio = price / dividend
            return ratio
        else:
            raise TypeError("The P/E ratio is not defined for this stock.")

    def record_trade(self, quantity_of_share, trade_indicator, trade_price):
        # type: (int, str, float) -> Trade
        """ Record a trade for a given stock with quantity of share, trade indicator, trade price.
        the trade indicator is either buy or sell """
        try:
            trade = Trade(self.stock_symbol, time.time(), quantity_of_share, trade_indicator, trade_price)
            self.all_trades.append(trade)
            print ("A new trade is added.")
        except:
            raise TypeError("Failure to add a new trade.")

    @property
    def calculate_volume_stock_price(self):
        """ Given a stock it calculates volume stock price based on trade in past 15 minuets"""
        trade_price_times_quantity = 0.0
        sum_quantity = 0
        index = get_index_binary_search(self.all_trades, time.time()-self.FIFTEEN_MINUTES)
        for a_trade in self.all_trades[index:]:
            trade_price_times_quantity += a_trade.quantity_of_share * a_trade.trade_price
            sum_quantity += a_trade.quantity_of_share

        if sum_quantity == 0:
            raise ValueError("Quantity of shares were zero when stock recorded.")
        else:
            return trade_price_times_quantity / float(sum_quantity)

    @property
    def stock_last_trade_price(self):
        """ Find the latest trade recorded and the latest price for a given stock"""
        try:
            return self.all_trades[-1].trade_price
        except IndexError:
            raise TypeError("No trade records available.")

