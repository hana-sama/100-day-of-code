import requests
import os

KIWI_API = os.environ['KIWI_API']
APP_ID = os.environ['APP_ID']
SHEETY_API_KEY = os.environ['API_KEY']
MY_TOKEN = os.environ['MY_TOKEN']
SHEET_ENDPOINT = "https://api.sheety.co/9e8f470eefba157500253cd11e49de60/personalFlightClub/prices"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": SHEETY_API_KEY,
}

bearer_headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}

class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}
    #This class is responsible for talking to the Google Sheet.
    
    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data
    
    def update_desination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url= f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=bearer_headers,
            )
            print(response.text)