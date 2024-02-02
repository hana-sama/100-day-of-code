import smtplib, ssl
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "hmama8989@gmail.com"
    password = GMAIL_APP_PASSWORD

    receiver = "ys.seki@nifty.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)