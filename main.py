import requests
from datetime import datetime
import os
GENDER = "Female"
WEIGHT_KG = "51"
HEIGHT_CM = "174"
AGE = "25"

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
MY_TOKEN = os.environ['MY_TOKEN']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/9e8f470eefba157500253cd11e49de60/myWorkoutsForHana/workouts"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {MY_TOKEN}"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

print(sheet_response)