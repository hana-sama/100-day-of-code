import os
import requests
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.TELEGRAM_CHAT_ID = TELEGRAM_CHAT_ID
        self.TTELEGRAM_BOT_TOKEN = TELEGRAM_BOT_TOKEN

    def send_sms(self, message):
        send_text = 'https://api.telegram.org/bot' + self.TTELEGRAM_BOT_TOKEN + '/sendMessage?chat_id=' + self.TELEGRAM_CHAT_ID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)
        # Prints if successfully sent.
        print(message)