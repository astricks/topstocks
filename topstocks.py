import sys
import collections

def incrementStockConsistency(stock, value):
    current_value = 0;
    if stock in consistentStocks:
        current_value = consistentStocks[stock]

    current_value = current_value + value;
    consistentStocks[stock] = current_value

f = open("stocks", "r")

m6, y1, y3, y5, y10, stockArray = ([], ) * 6

for line in f:
    stockArray.append(line.rstrip())

m6 = stockArray[0:250]
y1 = stockArray[250:500]
y3 = stockArray[500:750]
y5 = stockArray[750:1000]
y10 = stockArray[1000:1250]

stockArray = list(set(stockArray))

consistentStocks = {}

for stock in stockArray:
    if (stock in m6):
        incrementStockConsistency(stock, 1000)
    if (stock in y1):
        incrementStockConsistency(stock, 500)
    if (stock in y3):
        incrementStockConsistency(stock, 250)
    if (stock in y5):
        incrementStockConsistency(stock, -2500)
    if (stock in y10):
        incrementStockConsistency(stock, -5000)

for key in consistentStocks:
    if (consistentStocks[key] > 0):
        print key + ":" + str(consistentStocks[key])
