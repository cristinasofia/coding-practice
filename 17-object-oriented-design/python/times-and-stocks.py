from collections import Counter
import operator
class StockDict(Counter):
    
    def __init__(self):
        self.d = Counter()

    def update(self, timestamp, price):
        self[timestamp] = price

    def add(self, timestamp, price):
        self[timestamp] = price

    def delete(self, timestamp):
        del self[timestamp]

    def get_maxprice(self):
        # max(self.values())
        return max(self.iteritems(), key = operator.itemgetter(1))[1]

    def get_minprice(self):
        # min(self.values())
        return min(self.iteritems(), key = operator.itemgetter(1))[1]
    
    def get_latest(self):
        # max(self.d.keys())
        return max(self.iteritems(), key = operator.itemgetter(0))[0]

stocks = StockDict()
stocks.add(1, 100)
print(stocks)
stocks.add(2, 200)
print(stocks)
stocks.add(3, 300)
print(stocks)
stocks.add(4, 150)
print(stocks)
print(stocks.get_maxprice())
print(stocks.get_minprice())
print(stocks.get_latest())
stocks.update(3, 10)
stocks.delete(4)
print(stocks)
print(stocks.get_maxprice())
print(stocks.get_minprice())
print(stocks.get_latest())