!pip install pandas
!pip install requests
!pip install stockstats

import requests
import pandas as pandas
from stockstats import StockDataFrame

getYourApiData = requests.get("https://dsolvemern.herokuapp.com/api/weeklyinterval/YOURAPIKEY")
YourApiData = getYourApiData.json()

open = []
close = []
high = []
low = []
volume = []
amount = []

for i in YourApiData:
    iopenprice = i['openprice']
    open.append(iopenprice)
    icloseprice = i['closeprice']
    close.append(icloseprice)
    ihighprice = i['highprice']
    high.append(ihighprice)
    ilowprice = i['lowprice']
    low.append(ilowprice)
    ivolume = i['volume']
    volume.append(ivolume)
    amount.append(ivolume)

YourDataFrame = pandas.DataFrame({
    "open": open,
    "close": close,
    "high": high,
    "low": low,
    "volume": volume,
    "amount": amount,            
})

YourIndicator = StockDataFrame.retype(YourDataFrame)
YourIndicator['rsi_14'] = YourIndicator.get('rsi_14')

print(YourIndicator)
