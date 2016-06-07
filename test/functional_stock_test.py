from src.Stock import Stock
from src.GBCE import *
import unittest


class StockTest(unittest.TestCase):
    """ Test Simple stock functions."""
    stock_TEA = Stock("TEA", "Common", 0, 0, 100)
    stock_POP = Stock("POP", "Common", 8, 0, 100)
    stock_ALE = Stock("ALE", "Common", 23, 0, 60)
    stock_GIN = Stock("GIN", "Preferred", 8, 2, 100)
    stock_JOE = Stock("JOE", "Common", 13, 0, 250)

    def test_record_trade(self):
        """ Does it record a trade successfully. """
        self.trade_paremter= list()
        for indicator_iter in {"Sell", "Buy", "Invalid_indicator"}:
            for quantity_share_iter in range(0,100,1):
                for prince_iterator in range(0,1000,2):
                    self.trade_paremter.append([quantity_share_iter, indicator_iter, prince_iterator])




        self.assertIsNone(self.stock_ALE.record_trade(5, "sell", 4))

    """ record four trades for testing the list of all trades"""
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
        self.assertEqual(len(self.stock_TEA.all_trades), 2)

    def test_dividend_yield(self):
        """ Test answer  dividend yield calculation is correct."""

        self.assertEqual(self.stock_TEA.dividend_yield(3), 2)

    def test_calculate_pe_ratio(self):
        """ Test answer  P/E ratio  calculation is correct."""

        self.assertEqual(self.stock_TEA.calculate_pe_ratio(3), 1)

    def test_calculate_volume_stock_price(self):
        """ Test answer  calculate volume stock price is correct."""
        self.assertEqual(self.stock_TEA.calculate_volume_stock_price, 6.07)


if __name__ == '__main__':
    unittest.main()

