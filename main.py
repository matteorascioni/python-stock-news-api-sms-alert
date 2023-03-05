# Before to run this program this program run this commands:
# python3 -m venv venv
# pip3 install requests
# pip3 install twilio
import html
from twilio.rest import Client
from news_data import three_articles 
from alpha_vantage_data import data as alpha_vantage_data
from alpha_vantage_data import STOCK

# Twilio Account: (https://www.twilio.com/)
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

# Alpha Vantage Data
stock_data_list = [value for (key,value) in alpha_vantage_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# Calculate the difference between closing prices
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff_percent) > 1:
    # News data
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    for article in formatted_articles:
        # Send the sms
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER
            to=VERIFIED_NUMBER
        )   