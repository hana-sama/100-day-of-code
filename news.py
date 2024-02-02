import requests

url = "https://newsnow.p.rapidapi.com/"

payload = {
	"text": "Europe",
	"region": "wt-wt",
	"max_results": 25
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a4c97e0b9cmsh607eb19dad8854cp175929jsnbd0edb3d64c3",
	"X-RapidAPI-Host": "newsnow.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())