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
