import requests
import os
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = ""
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_API,
}
response = requests.get(url=STOCK_ENDPOINT, params=alpha_vantage_parameters)
response.raise_for_status
data = response.json()['Time Series (Daily)']
print(data)
stock_price_data_list = [value for (key, value) in data.items()]
yesterday_data = stock_price_data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_data = stock_price_data_list[1]
day_before_closing_price = day_before_data['4. close']
price_change = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = None
if price_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_change = f"{((price_change / float(yesterday_closing_price)) * 100):.2f}"
print(percentage_change)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_change) > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = response.json()
    top_three_articles = articles['articles'][0:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_change}$\nHeadline: {article['title']}. \nBrief: {article['description']}"for article in top_three_articles]

    for article in formatted_articles:
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        bot_chatID = os.environ.get("TELEGRAM_CHAT_ID")
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + article
        response = requests.get(send_text)
else:
    print("No need to update news for this stock.")


   