""" Contains Stock class and methods"""

import time
from Trade import Trade


# create class stock
class Stock(object):
    FIFTEEN_MINUTES = 15 * 60  # constant for converting 15 minutes to second, use it for retrieving recorded trades

    def __init__(self, stock_symbol, stock_type, last_dividend, fixed_dividend, par_value, stock_price=0):
        # type: (str, str, int, float, int, float) -> Stock

        self.stock_symbol = stock_symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.stock_price = stock_price
        self.all_trades = list()  # a list to keep track of all trades

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

    @property
    def last_dividend(self):
        return self._last_dividend

    @last_dividend.setter
    def last_dividend(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError('The value of the last dividend should be a number.')
        self._last_dividend = value

    @property
    def fixed_dividend(self):
        return self._fixed_dividend

    @fixed_dividend.setter
    def fixed_dividend(self, value):
        if not isinstance(value, (int, long, float)) and not value:
            raise TypeError('The value of the last dividend should be a number or an empty string.')
        self._fixed_dividend = value

    @property
    def par_value(self):
        return self._par_value

    @par_value.setter
    def par_value(self, value):
        if not isinstance(value, (int, long)):
            raise TypeError('The value of the Par Value should be an integer.')
        self._par_value = value

    @property
    def stock_price(self):
        return self._stock_price

    @stock_price.setter
    def stock_price(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError('The value of price should be a number.')
        self._stock_price = value

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
        # type: (int, str, float) -> Trade

        """ Record a trade for a given stock with quantity of share, trade indicator, trade price.
        the trade indicator is either buy or sell """

        trade_time = time.time()  # current time
        try:
            trade = Trade(self.stock_symbol, trade_time, quantity_of_share, trade_indicator, trade_price)
            self.all_trades.append(trade)
            print ("Adding a new trade was successful.")
        except:
            raise TypeError("Adding a new trade was not successful.")

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
                if current_time <= a_trade.trade_time + self.FIFTEEN_MINUTES:
                    trade_price_times_quantity += a_trade.quantity_of_share * a_trade.trade_price
                    sum_quantity += a_trade.quantity_of_share
            if sum_quantity == 0:
                print "Quantity of shares were zero when stock recorded."
            else:
                return float(trade_price_times_quantity) / float(sum_quantity)

    @property
    def stock_last_trade_price(self):
        """ Find the latest trade recorded and the latest price for a given stock"""

        num_recorded_trades = len(self.all_trades)
        latest_trade = self.all_trades[num_recorded_trades-1]
        latest_trade_price = latest_trade.trade_price
        return latest_trade_price
