import stockDataClient
import sp500data
import dow30data
import numpy
getLastDays = stockDataClient.getLastDays
sp500data = sp500data.data
dow30data = dow30data.data
print(len(sp500data))
print(len(dow30data))
print(getLastDays("AAPL",5))
