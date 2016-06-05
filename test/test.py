from src.funcs import *

stock_TEA = Stock("TEA", "Common", 8, 7, 100)
stock_GIN = Stock("GIN", "Common", 2, 3, 12)


stock_TEA.record_trade(2, "sell", 8)
stock_GIN.record_trade(7, "sell", 7)
# time.sleep(10)
stock_TEA.record_trade(5, "buy", 12)
stocks= {stock_TEA, stock_GIN}
print calculate_gbce(stocks)

for item in stock_TEA.all_trades:
    print item.trade_price

print "latest trade %s" % stock_TEA.stock_last_trade_price

print stock_TEA.stock_symbol
