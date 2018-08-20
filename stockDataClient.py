import pandas
pandas.core.common.is_list_like = pandas.api.types.is_list_like
from pandas_datareader import data, wb
import datetime

def getLastDays(stock, numDays, source = "iex"):
    numDays = numDays + 1
    start = datetime.date.today() - datetime.timedelta(days = numDays)
    end = datetime.date.today()
    
    dataFrame = data.DataReader(stock, source, start, end)
    tradeDays = []
    for day in range(0,numDays-1):
        dayData = {
            "day": day,
            "open": dataFrame.iat[day,0],
            "high": dataFrame.iat[day,1],
            "low": dataFrame.iat[day,2],
            "close": dataFrame.iat[day,3]
        }
        tradeDays.append(dayData)
    return tradeDays
