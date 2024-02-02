import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
RAPID_API_KEY = os.environ.get("RAPID_API_KEY")
url = "https://newsnow.p.rapidapi.com/"

payload = {
	"text": "Europe",
	"region": "wt-wt",
	"max_results": 25
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": "newsnow.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)
articles = response.json()
top_ten_articles = articles['articles'][0:10]