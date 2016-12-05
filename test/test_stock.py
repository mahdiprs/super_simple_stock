""" Unittest for creating stock class an its method """

from src.Stock import Stock
import unittest


class StockTest(unittest.TestCase):
    """ Test  stock functions."""
    stock_TEA = Stock("TEA", "Common", 0, 0, 100)
    stock_POP = Stock("POP", "Common", 8, 0, 100)
    stock_ALE = Stock("ALE", "Common", 23, 0, 60)
    stock_GIN = Stock("GIN", "Preferred", 8, 2, 100)
    stock_JOE = Stock("JOE", "Common", 13, 0, 250)

    def test_record_trade(self):
        """ Does it record a trade successfully. """

        self.assertIsNone(self.stock_ALE.record_trade(5, "sell", 4))
        self.assertRaises(TypeError, self.stock_ALE.record_trade, "", "sell", 1)
        self.assertRaises(TypeError, self.stock_ALE.record_trade, 2, "sell", "c")
        self.assertIsNone(self.stock_JOE.record_trade(5, "buy", 2))
        self.assertIsNone(self.stock_POP.record_trade(5, "buy", 4))
        self.assertRaises(TypeError, self.stock_POP.record_trade, 5, "Bell", 4)

    """ record four trades for testing the list of all trades"""
    stock_TEA.record_trade(2, "sell", 3)
    stock_TEA.record_trade(5, "buy", 4)
    stock_GIN.record_trade(7, "sell", 7)
    stock_GIN.record_trade(7, "sell", 8)

    stocks = {stock_TEA, stock_GIN}

    def test_get_all_trades(self):
        """ Check all trades recorded """
        self.assertNotEqual(len(self.stock_TEA.all_trades), 7)
        self.assertEqual(len(self.stock_TEA.all_trades), 2)

    def test_dividend_yield(self):
        """ Test answer  dividend yield calculation is correct."""

        self.assertNotEqual(self.stock_TEA.dividend_yield(3), 2)

    def test_calculate_pe_ratio(self):
        """ Test answer  P/E ratio  calculation is correct."""

        self.assertRaises(TypeError, self.stock_TEA.calculate_pe_ratio, 3)

    def test_calculate_volume_stock_price(self):
        """ Test answer  calculate volume stock price is correct."""

        self.assertNotEqual(self.stock_TEA.calculate_volume_stock_price, 6.07)


if __name__ == '__main__':
    unittest.main()

