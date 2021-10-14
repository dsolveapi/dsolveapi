!pip install plotly
import requests
import plotly.express
import plotly.graph_objects as go

#Bitcoin Weather Free "https://dsolvemern.herokuapp.com/api/bitcoinweatherfree/YOURAPIKEY"
getYourApiData = requests.get("https://dsolvemern.herokuapp.com/api/bitcoinweather/YOURAPIKEY")
YourApiData = getYourApiData.json()

#Most Recent Date API Data
YourApiDataToday = YourApiData[-1]
btcweather = YourApiDataToday['btc_weather']

#Chart Your Recent Weather
#Most Recent 500 Days
NumberofDays = len(YourApiData)
YourApiData = YourApiData[NumberofDays - 500:NumberofDays]

#Empty Boxes
date = []
closeprice = []
color = []
macdweekly = []
histogramweekly = []
signalweekly = []
macddaily = []
histogramdaily = []
signaldaily = []

#Fill the Empty Boxes (Simple Loop)
#Learn More (https://www.learnpython.org/en/Loops)
for i in YourApiData:
    idate = i['date']
    date.append(idate)
    icloseprice = i['closeprice']
    closeprice.append(icloseprice)
    icolor=  i['btc_weather_color']
    color.append(icolor)
    imacdweekly=  i['macd_line_weekly']
    macdweekly.append(imacdweekly)
    ihistogramweekly = i['histogram_weekly']
    histogramweekly.append(ihistogramweekly)
    isignalweekly = i['signal_line_weekly']
    signalweekly.append(isignalweekly)
    imacddaily=  i['macd_line_daily']
    macddaily.append(imacddaily)
    ihistogramdaily = i['histogram_daily']
    histogramdaily.append(ihistogramdaily)
    isignaldaily = i['signal_line_daily']
    signaldaily.append(isignaldaily)

#Weather Chart
chartWeather = plotly.express.bar(x=date, y=closeprice)
chartWeather.update_layout(plot_bgcolor='white')
chartWeather.update_traces(marker_color=color)

#Weekly Chart
chartWeekly = plotly.express.line(x=date, y=macdweekly)
chartWeekly.update_traces(line_color="black")
chartWeekly.add_trace(go.Scatter(x=date, y=signalweekly, fill='tozeroy', line=dict(color="red"), name="signal" ))
chartWeekly.add_trace(go.Bar(x=date, y=histogramweekly, marker_color="blue", name="histogram"))
chartWeekly.update_layout(plot_bgcolor='white')

#Daily Chart
chartDaily = plotly.express.line(x=date, y=macddaily)
chartDaily.update_traces(line_color="black")
chartDaily.add_trace(go.Scatter(x=date, y=signaldaily, fill='tozeroy', line=dict(color="red"), name="signal"))
chartDaily.add_trace(go.Bar(x=date, y=histogramdaily, marker_color="blue", name="histogram"))
chartDaily.update_layout(plot_bgcolor='white')

print('Bitcoin Weather')
print(btcweather)
print('Weather Charts')
chartWeather.show()
chartWeekly.show()
chartDaily.show()
