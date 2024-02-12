import datetime
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_data(place, forecast_days=None, kind=None):
    OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
    OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
    api_key = os.environ.get("OPEN_WEATHER_API_KEY")
    weather_params = {
        # "lat": 35.689487,
        # "lon": 139.691711,
        "q": place,
        "cnt": 8 * forecast_days,
        "appid": api_key,
    }
    response = requests.get(url=OWN_ENDPOINT, params=weather_params)
    response.raise_for_status
    data = response.json()
    filtered_data = data['list']
    nr_values = (8 * forecast_days)
    filtered_data = filtered_data[0:nr_values]
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    dt = datetime.datetime.now()
    d_truncated = datetime.date(dt.year, dt.day, dt.month)
    dates = [d_truncated]
    for i in range(0, forecast_days - 1):
        next_day = d_truncated + datetime.timedelta(days=1)
        dates.append(next_day)
        d_truncated = next_day
    temperatures = [10, 11, 15]
    temperatures = [forecast_days * i for i in temperatures]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="London", forecast_days=2, kind="Sky"))