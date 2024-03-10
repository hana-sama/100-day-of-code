import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TELEGRAM_BOT_KEY = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT_CHATID = os.environ.get("TELEGRAM_BOT_CHAT_ID")
BASE_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/'
print(TELEGRAM_BOT_KEY, BOT_CHATID)
class TelegramBot:
      def __init__(self):
          self.api_key = TELEGRAM_BOT_KEY
          self.chat_id = BOT_CHATID
          
      def send(self, text):
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage'
        # files = {'document': open(document_path, 'rb')}
        data = {'chat_id': self.chat_id,
                'text': text}
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            print("Message sent successfully")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    telegram_bot = TelegramBot()
    telegram_bot.send(text="Hello, Angela!")