from src.Stock import Stock
from src.GBCE import *
import unittest


class TradeTest(unittest.TestCase):
    """ Test Stock class and methods."""
    stock_TEA = Stock("TEA", "Common", 0, 0, 100)
    stock_GIN = Stock("GIN", "Preferred", 8, 2, 100)

    """ Record four trades for testing the list of all trades"""
    stock_TEA.record_trade(2, "sell", 3)
    stock_TEA.record_trade(5, "buy", 4)
    stock_GIN.record_trade(7, "sell", 7)
    stock_GIN.record_trade(7, "sell", 8)

    stocks = {stock_TEA, stock_GIN}

    def test_stock_last_trade_price(self):
        """ Test the method returns the latest price of a stock properly"""

        self.assertEqual(self.stock_TEA.stock_last_trade_price, 4)
        self.assertEqual(self.stock_TEA.stock_last_trade_price, 5)

    def test_calculate_gbce(self):
        """ Test the GBCE function """
        self.assertEqual(calculate_gbce(self.stocks), 7)


if __name__ == '__main__':
    unittest.main()
