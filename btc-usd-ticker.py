#!/usr/bin/env python

import httplib
import urllib
import json
from threading import Timer

count = 0
lastPrice = 0

def getTicker():
    Timer(15.0, getTicker).start()
    conn = httplib.HTTPSConnection("btc-e.com")
    conn.request("GET", "/api/2/btc_usd/ticker")
    response = conn.getresponse()
    
    data = json.load(response)    
    printTickerData(data)

    conn.close()

def priceChange(oldPrice, newPrice):
    change = newPrice - oldPrice
    if change < 0:
        return "{0:.3f}".format(change)
    elif change == 0:
        return "===="
    else:
        return "+" + "{0:.3f}".format(change)

def printTickerData(data):
    global count
    global lastPrice

    printLastDelta(count, data)
    print "| HIGH - " + str(data['ticker']['high']),
    print "| LOW - " + str(data['ticker']['low']),
    print "| run#" + str(count)

    count += 1
    lastPrice = data['ticker']['last']

def printLastDelta(count, data):
    if count == 0:
        print "LAST - " + str(data['ticker']['last']) + "(====)",    
    else :
        print "LAST - " + str(data['ticker']['last']) + "(" + priceChange(lastPrice, data['ticker']['last']) + ")",

getTicker()
