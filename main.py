import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from send_email import send_email
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

url = "https://newsapi.org/v2/everything"

API_KEY = os.environ.get("NEWS_API_KEY")
BOT_KEY = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT_CHATID = os.environ.get("TELEGRAM_BOT_CHAT_ID")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

def search_news_and_email():
    query = input("Please write topic you want to search: ")
    news_params = {
        "q": query,
        "language": "en",
        "apikey": API_KEY
    }
    response = requests.get(url, params=news_params)
    articles = response.json()
    top_five_articles = articles['articles'][0:5]
    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']} \nUrl for this story: {article['url']}" for article in top_five_articles]

    # Send summary of articles to Telegram
    for article in formatted_articles:
        bot_token = BOT_KEY
        bot_chatID = BOT_CHATID
        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={article}'
        response = requests.get(send_text)

    # Send summary of articles via email
    # body = ''
    # for article in articles['articles'][0:20]:
    #     if article['title'] is not None and article['description'] is not None:
    #         body = "Subject: Today's news" + "\n" + body +  article["title"] + "\n" + article["description"] + "\n" + article['url'] + 2*"\n"
    # body = body.encode("utf-8")
    # send_email(message=body)


if __name__ == '__main__':
    search_news_and_email()