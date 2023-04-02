import requests
import datetime
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#Put your values here
STOCK_NAME = 
COMPANY_NAME = 
STOCK_KEY = 
NEWS_KEY = 
SMS_SID = 
SMS_TOKEN = 
SMS_SENDER = 
SMS_RECEIVER = 
YESTERDAY = datetime.date.today() - datetime.timedelta(days=1)
DAYBFRYES = datetime.date.today() - datetime.timedelta(days=2)

stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_KEY}"
req1 = requests.get(stock_url)
data1 = req1.json()

close1 = float(data1["Time Series (Daily)"][f"{YESTERDAY}"]["4. close"])
close2 = float(data1["Time Series (Daily)"][f"{DAYBFRYES}"]["4. close"])
diff = round(close1 - close2, 2)
print(diff)
if diff<0:
    arrow="down"
else:
    arrow="up"
percent_diff = round((abs(diff) / close1) * 100, 2)
print(percent_diff)
if percent_diff > 5:
    news_url = f"https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey={NEWS_KEY}"
    req2 = requests.get(news_url)
    data2 = req2.json()
    descriptons = [i["description"] for i in data2["articles"]]
    titles = [i["title"] for i in data2["articles"]]
    news=[[titles[i],descriptons[i]] for i in range(len(titles))]
    client = Client(SMS_SID,SMS_TOKEN)

    for i in (news):
        if arrow=="down":
            message = message = client.messages.create(
                    body=f"{STOCK_NAME}: 🔻 {percent_diff} %\nHeadline: {i[0]}\nDescription: {i[1]}", from_=SMS_SENDER, to=SMS_RECEIVER
                )
            print(message.sid)
        else:
            message = message = client.messages.create(
                    body=f"{STOCK_NAME}: 🔺 {percent_diff} %\nHeadline: {i[0]}\nDescription: {i[1]}", from_=SMS_SENDER, to=SMS_RECEIVER
                )
            print(message.sid)


