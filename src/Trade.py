""" Contains Trade class"""


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

    @property
    def quantity_of_share(self):
        return self._quantity_of_share

    @quantity_of_share.setter
    def quantity_of_share(self, value):
        if not isinstance(value, (int, long)):
            raise TypeError('The value of quantity of share should be an integer number.')
        self._quantity_of_share = value

    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError('The value of price should be a number.')
        self._trade_price = value
