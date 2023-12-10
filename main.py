import requests
import json
import os

def get_crypto_current_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    crypto_parameters = {
    'symbol':'BTC',
    'convert':'USD'
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'CMC_API',
    }

    response = requests.get(url, headers=headers, params=crypto_parameters)
    data = response.json()
    current_btc_price = data['data']['BTC']['quote']['USD']['price']

    return current_btc_price

price_change_percentage_24h = 0
def get_crypto_price_change():
    global price_change_percentage_24h
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    crypto_parameters = {
    'symbol':'BTC',
    'convert':'USD'
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'CMC_API',
    }

    response = requests.get(url, headers=headers, params=crypto_parameters)
    data = response.json()
    price_change_percentage_24h = data['data']['BTC']['quote']['USD']['percent_change_24h']

    if price_change_percentage_24h >= 2:
        return "rise"
    elif price_change_percentage_24h <= - 2:
        return 'fall'


top_news_list = []
def get_crypto_news():
    global top_news_list
    # Set up the API endpoint URL
    url = "https://cryptopanic.com/api/v1/posts/"
    
    crypto_parameters = {
        "auth_token": "CRYPTO_NEWS_API",
        "currencies": "BTC",
        "filter": "important",
    }

    headers = {
    "Accepts": "application/json"
    }
    # Make an HTTP request to the API endpoint
    response = requests.get(url, headers=headers, params=crypto_parameters)
    # Parse the JSON response
    data = json.loads(response.text)

    news = data['results']
    # Use the news in your Python program
    for article in news:
        top_news = {}
        top_news['title'] = article['title']
        top_news['url'] = article['url']
        top_news['published_at'] = article['published_at']
        top_news_list.append(top_news)
    return top_news_list

up_down = None
if price_change_percentage_24h > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
bot_message = ''
def create_bot_message():
    global bot_message
    result = get_crypto_news()

    formatted_articles = [f"BTC: {up_down}{abs(price_change_percentage_24h):.2f}%\nHeadline: {article['title']}. \nurl: {article['url']}\nPublished at: {article['published_at']}"for article in top_news_list]
    
    for article in formatted_articles:
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        bot_chatID = os.environ.get("TELEGRAM_CHAT_ID")
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + article
        response = requests.get(send_text)


get_crypto_price_change()
create_bot_message()