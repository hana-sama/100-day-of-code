import requests
import os
# How to create environment variables
# 1. import osmodule
# 2. In terminal, export XXX_API_KEY=your_api_key
# 3. In terminal, type 'env' to check stored environment variables
# 4. In editor, type os.environ.get("your environment variables") 

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 35.689487,
    "lon": 139.691711,
    "cnt": 4,
    "appid": api_key,
}


def get_weather_forecast():
    response = requests.get(url=OWN_ENDPOINT, params=weather_params)
    response.raise_for_status
    weather_data = response.json()
    weather_list = weather_data['list']
    will_rain = False
    for hour_data in weather_list:
        condition_code = hour_data['weather'][0]['id']
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        send_message = telegram_bot_send_text("It's going to rain today. Remeber to bring an ☂️.")
    else:
        send_message = telegram_bot_send_text("It's going to be 🌞 today. Have a nice day!")


def telegram_bot_send_text(bot_message):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    bot_chatID = os.environ.get("TELEGRAM_CHAT_ID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()


get_weather_forecast()