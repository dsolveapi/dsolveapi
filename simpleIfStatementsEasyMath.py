!pip install plotly
import requests
import plotly.express

#Bitcoin Weather Free "https://dsolveapi.herokuapp.com/api/bitcoinweatherfree/YOURAPIKEY"
getYourApiData = requests.get("https://dsolveapi.herokuapp.com/api/bitcoinweather/YOURAPIKEY")
YourApiData = getYourApiData.json()

#Last Date API Data
YourApiDataCurrent = YourApiData[-1]

#Simple If Statements
#Weekly Points
#If MACD Line > 0 30 Points | If MACD Line <= 0 0 Points
if YourApiDataCurrent['macd_line_weekly'] > 0:
    trendpointsweekly = 30
else: trendpointsweekly = 0

if YourApiDataCurrent['histogram_weekly'] > 0:
    trendstrengthpointsweekly = 30
else: trendstrengthpointsweekly = 0
   
if YourApiDataCurrent['macd_slope_weekly'] == 'slope +':
    momentumpointsweekly = 20
else: momentumpointsweekly = 0

if YourApiDataCurrent['histogram_slope_weekly'] == 'slope +':
    momentumconditionpointsweekly = 20
else: momentumconditionpointsweekly = 0

#Easy Math
btcpointsweekly = trendpointsweekly + trendstrengthpointsweekly + momentumpointsweekly + momentumconditionpointsweekly

#Simple If Statements
#Daily Points
if YourApiDataCurrent['macd_line_daily'] > 0 :
    trendpointsdaily = 30
else: trendpointsdaily = 0
    
if YourApiDataCurrent['histogram_daily'] > 0:
    trendstrengthpointsdaily = 30
else: trendstrengthpointsdaily = 0

if YourApiDataCurrent['signal_slope_daily'] == 'slope +':
    momentumpointsdaily = 20
else: momentumpointsdaily = 0

if YourApiDataCurrent['histogram_slope_daily'] == 'slope +':
    momentumconditionpointsdaily = 20
else: momentumconditionpointsdaily = 0

#Easy Math    
btcpointsdaily = trendpointsdaily + trendstrengthpointsdaily + momentumpointsdaily + momentumconditionpointsdaily

#Easy Math
#Change the Weightings
btcweather = (btcpointsdaily * 0.28) + (btcpointsweekly * 0.72)

#Chart Your Recent Weather
#Most Recent 500 Days
NumberofDays = len(YourApiData)
YourApiData = YourApiData[NumberofDays - 500:NumberofDays]

#Empty Boxes
date = []
closeprice = []
color = []

#Fill the Empty Boxes (Simple Loop)
#Learn More (https://www.learnpython.org/en/Loops)
for i in YourApiData:
    idate = i['date']
    date.append(idate)
    icloseprice = i['closeprice']
    closeprice.append(icloseprice)
    #Simple If Statment !!CHALLENGE Change the Colors!!
    if i['btc_weather'] > 50:
        icolor = "gold"
    else: icolor = "darkblue"
    color.append(icolor)

#Chart Bitcoin Weather
xaxis_data = date
yaxis_data = closeprice
yaxis_data_min = min(yaxis_data) 
yaxis_data_max = max(yaxis_data)    

yourChart = plotly.express.bar(x=xaxis_data, y=yaxis_data)
yourChart.update_layout(yaxis_range=[yaxis_data_min,yaxis_data_max], plot_bgcolor='white')
yourChart.update_traces(
    marker_color=color
)

print('Bitcoin Weather')
print(btcweather)
print('Weather Chart')
yourChart.show()
