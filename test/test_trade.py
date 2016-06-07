""" Unittest for creating Trades and other functions """


from src.Stock import Stock
from src.binary_search import *
import time
from src.GBCE import *
import unittest


class TradeTest(unittest.TestCase):
    """ Test Stock class and methods."""
    stock_TEA = Stock("TEA", "Common", 0, 0, 100)
    stock_GIN = Stock("GIN", "Preferred", 8, 2, 100)

    """ Record four trades for testing the list of all trades"""
    stock_TEA.record_trade(2, "sell", 3)
    time.sleep(20)
    stock_TEA.record_trade(5, "buy", 4)
    stock_GIN.record_trade(7, "sell", 7)
    stock_GIN.record_trade(7, "sell", 8)

    stocks = {stock_TEA, stock_GIN}

    def test_stock_last_trade_price(self):
        """ Test the method returns the latest price of a stock properly"""

        self.assertEqual(self.stock_TEA.stock_last_trade_price, 4)
        self.assertEqual(self.stock_TEA.stock_last_trade_price, 5)

    for item in stock_TEA.all_trades:
        print item.trade_time

    def test_get_index_binary_search(self):
        """Check returning the index of the first trad recorded in the last 15 minutes"""

        current_time = time.time()
        self.assertEqual(get_index_binary_search(self.stock_TEA.all_trades, current_time - 15), 0)
        self.assertEqual(get_index_binary_search(self.stock_TEA.all_trades, current_time - 15*60), 1)

    def test_calculate_gbce(self):
        """ Test the GBCE function """
        self.assertEqual(calculate_gbce(self.stocks), 7)


if __name__ == '__main__':
    unittest.main()
