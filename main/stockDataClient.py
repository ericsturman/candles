import pandas
pandas.core.common.is_list_like = pandas.api.types.is_list_like
from pandas_datareader import data, wb
import datetime

def getLastDays(stock, numDays, source = "iex"):
    numDays = numDays + 1
    start = datetime.date.today() - datetime.timedelta(days = numDays*2)
    end = datetime.date.today()
    
    dataFrame = data.DataReader(stock, source, start, end)
    actualLength = len(dataFrame["open"])
    tradeData = {
            "day": [],
            "open": [],
            "high": [],
            "low": [],
            "close": []
        }
    for day in range(actualLength-numDays+1,actualLength):
        tradeData["day"].append(day)
        tradeData["open"].append(dataFrame.iat[day,0])
        tradeData["high"].append(dataFrame.iat[day,1])
        tradeData["low"].append(dataFrame.iat[day,2])
        tradeData["close"].append(dataFrame.iat[day,3])
    return tradeData
