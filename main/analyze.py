#! /usr/bin/python3

import stockDataClient
import sp500data
import dow30data
import numpy
import talib

getLastDays = stockDataClient.getLastDays
sp500data = sp500data.data
dow30data = dow30data.data
for stock in dow30data: 
    stockLast = getLastDays(stock, 50)
    o = numpy.array(stockLast['open'], dtype=float)
    c = numpy.array(stockLast['close'], dtype=float)
    h = numpy.array(stockLast['high'], dtype=float)
    l = numpy.array(stockLast['low'], dtype=float)
    longLine = talib.CDLLONGLINE(o,h,l,c)
    shortLine = talib.CDLSHORTLINE(o,h,l,c)
    takuri = talib.CDLTAKURI(o,h,l,c)
    spinningTop = talib.CDLSPINNINGTOP(o,h,l,c)
    longLeggedDoji = talib.CDLLONGLEGGEDDOJI(o,h,l,c)
    highWave = talib.CDLHIGHWAVE(o,h,l,c)
    gravestoneDoji = talib.CDLGRAVESTONEDOJI(o,h,l,c)
    dragonflyDoji = talib.CDLDRAGONFLYDOJI(o,h,l,c)
    doji = talib.CDLDOJI(o,h,l,c)

    print("long line:     " + str(longLine[len(longLine)-1]))
    print("short line:    " + str(shortLine[len(shortLine)-1]))
    print("takuri:        " + str(takuri[len(takuri)-1]))
    print("spinning top:  " + str(spinningTop[len(spinningTop)-1]))
    print("long legged:   " + str(longLeggedDoji[len(longLeggedDoji)-1]))
    print("high wave:     " + str(highWave[len(highWave)-1]))
    print("gravestone:    " + str(gravestoneDoji[len(gravestoneDoji)-1]))
    print("dragon fly:    " + str(dragonflyDoji[len(dragonflyDoji)-1]))
    print("doji:          " + str(doji[len(doji)-1]))




