""" Contains Trade class"""


class Trade(object):
    def __init__(self, stock_symbol, trade_time, quantity_of_share, trade_indicator, trade_price):
        # type: (str, time, int, str, float) -> Trade
        self.stock_symbol = stock_symbol
        self.trade_time = trade_time
        self.quantity_of_share = quantity_of_share
        self.trade_indicator = trade_indicator
        self.trade_price = trade_price

    """Validate trade indicator type."""
    @property
    def trade_indicator(self):
        return self._trade_indicator

    @trade_indicator.setter
    def trade_indicator(self, value):
        if value.upper() not in {"BUY", "SELL"}:
            raise TypeError("Invalid trade indicator.")
        self._trade_indicator = value

    """Validate quantity of share type."""
    @property
    def quantity_of_share(self):
        return self._quantity_of_share

    @quantity_of_share.setter
    def quantity_of_share(self, value):
        if not isinstance(value, (int, long)):
            raise TypeError("Invalid quantity of share type.")
        self._quantity_of_share = value

    """Validate trade price type."""
    @property
    def trade_price(self):
        return self._trade_price

    @trade_price.setter
    def trade_price(self, value):
        if not isinstance(value, (int, long, float)):
            raise TypeError("Invalid trade price type.")
        self._trade_price = value