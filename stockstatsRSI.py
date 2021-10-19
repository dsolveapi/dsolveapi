!pip install pandas
!pip install requests
!pip install stockstats

import requests
import pandas as pandas
from stockstats import StockDataFrame

#Daily "https://dsolveapi.herokuapp.com/api/dailyinterval/YOURAPIKEY"
getYourApiData = requests.get("https://dsolveapi.herokuapp.com/api/weeklyinterval/YOURAPIKEY")
YourApiData = getYourApiData.json()

#Empty Boxes
open = []
close = []
high = []
low = []
volume = []
amount = []

#Fill the Empty Boxes (Simple Loop)
#Learn More (https://www.learnpython.org/en/Loops)
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

#Calculate RSI Indicator
#YourIndicator['boll'] = YourIndicator.get('boll') (Bollinger Bands)
#YourIndicator['macd'] = YourIndicator.get('macd') (MACD)
YourIndicator = StockDataFrame.retype(YourDataFrame)
YourIndicator['rsi_14'] = YourIndicator.get('rsi_14')

print(YourIndicator)
