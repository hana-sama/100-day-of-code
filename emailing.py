import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id = os.environ.get("TELEGRAM_BOT_CHAT_ID")

BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

def send_sns(document_path):
    url = BASE_URL + 'sendDocument'
    files = {'document': open(document_path, 'rb')}
    data = {'chat_id': chat_id,
            'caption': "Unidentified Object Detected!"}
    response = requests.post(url, files=files, data=data)
    return response.json()

