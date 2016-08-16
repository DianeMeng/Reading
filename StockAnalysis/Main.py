

import csv
import Stock
from itertools import *
import numpy as np
import datetime

# load raw data,get a list<stock>
def loaddata(path):
    stocklist = []
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        header =next(spamreader)
        for row in spamreader:
            s = Stock.Stock(row[0],np.float(row[1]),np.float(row[2]),np.float(row[3]),np.float(row[4]),np.float(row[5]),np.float(row[6]))
            stocklist.append(s)
    return header,stocklist

#check the increment of price
def _valid_price(g):
    return ((max(g) - min(g)) /min(g)) < 0.223

#group by date and generate one record for each day
def groupbyday(stocklist):
    dayrecord = []
    keyfn =  lambda s: s.date #key for group

    fopening_price= lambda g: _valid_price(g) and g[0] or 0
    fceiling_price=lambda g: _valid_price(g) and max(g) or 0
    ffloor_price=lambda g: _valid_price(g) and min(g) or 0
    fclosing_price=lambda g: _valid_price(g) and g[-1] or 0

    for k, v in groupby(stocklist, keyfn):
        pricelists = [[] for i in range(4)]
        volumelist=[]
        amountlist=[]
        for value in v:
            pricelists[0].append(value.opening_price)
            pricelists[1].append(value.ceiling_price)
            pricelists[2].append(value.floor_price)
            pricelists[3].append(value.closing_price)
            volumelist.append(value.volume)
            amountlist.append(value.amount)
            # print(value)
        onerecored=Stock.Record(k,ffloor_price(pricelists[2]),fopening_price(pricelists[0]),fceiling_price(pricelists[1]),sum(volumelist),sum(amountlist),fclosing_price(pricelists[3]))
        # print(onerecored)
        dayrecord.append(onerecored)
    return dayrecord

#generate range date
def datetimeGenerator(from_date, to_date):
    from datetime import timedelta
    if from_date > to_date:
        return
    else:
        while from_date <= to_date:
            yield from_date
            from_date = from_date + timedelta(days=1)
        return

#each day get a index
def indexdate(dayrecord):
    l = len(dayrecord)
    start = dayrecord[0:1][0].date
    end = dayrecord[l - 1: l][0].date
    start_time = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_time= datetime.datetime.strptime(end, '%Y-%m-%d')
    return datetimeGenerator(start_time,end_time)



def main():
    path="C:/Users/dan/PycharmProjects/StockAnalysis/Rawdata/SH600690.csv"
    header,stocklist = loaddata(path)
    # for x in stocklist[:5]:
    #    print(x)
    dayrecord=groupbyday(stocklist)
    # for i in dayrecord:
    #     print(i)
    dateRange = indexdate(dayrecord)
    for d in dateRange:
        print(d)



if __name__ == '__main__':
    main()