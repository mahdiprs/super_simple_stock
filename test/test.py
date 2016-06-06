from src.Stock import Stock
from src.GBCE import *
import unittest

print not isinstance(2, (int, long, float))


class SimpleStockMarketTest(unittest.TestCase):
    """ Test Simple stock functions."""
    stock_TEA = Stock("TEA", "Common", 0, 0, 100)
    stock_POP = Stock("POP", "Common", 8, 0, 100)
    stock_ALE = Stock("ALE", "Common", 23, 0, 60)
    stock_GIN = Stock("GIN", "Preferred", 8, 2, 100)
    stock_JOE = Stock("JOE", "Common", 13, 0, 250)

    def test_record_trade(self):
        """ Does it record a trade successfully. """

        self.assertIsNone(self.stock_TEA.record_trade(2, "sell", 1))
        self.assertIsNone(self.stock_TEA.record_trade(5, "buy", 2))
        self.assertIsNone(self.stock_POP.record_trade(5, "buy", 4))
        self.assertIsNone(self.stock_POP.record_trade(5, "Bell", 4))

    """ record two trades for testing the list of all trades"""
    stock_TEA.record_trade(2, "sell", 3)
    stock_TEA.record_trade(5, "buy", 4)
    stock_GIN.record_trade(7, "sell", 7)
    stock_GIN.record_trade(7, "sell", 8)

    stocks = {stock_TEA, stock_GIN}

    for item in stock_TEA.all_trades:
        print (item.trade_price)


    def test_get_all_trades(self):
        """ Check all trades recorded """
        self.assertEqual(len(self.stock_TEA.all_trades), 7)

    def test_dividend_yield(self):
        """ Test answer  dividend yield calculation is correct."""

        self.assertEqual(self.stock_TEA.dividend_yield(3), 2)

    def test_calculate_pe_ratio(self):
        """ Test answer  P/E ratio  calculation is correct."""

        self.assertEqual(self.stock_TEA.calculate_pe_ratio(3), 1)

    def test_calculate_volume_stock_price(self):
        """ Test answer  calculate volume stock price is correct."""
        self.assertEqual(self.stock_TEA.calculate_volume_stock_price, 6.071428571428571)

    def test_stock_last_trade_price(self):
        """ Test the method returns the latest price of trades properly"""

        self.assertEqual(self.stock_TEA.stock_last_trade_price, 4)

    def test_calculate_gbce(self):
        """ Test the GBCE function """
        self.assertEqual(calculate_gbce(self.stocks),7)


if __name__ == '__main__':
    unittest.main()
