import requests
import datetime
# Response Code means:
# 1xxx: Hold on
# 2xxx: Here you go
# 3xxx: Go away
# 4xxx: You screwed up
# 5xxx: I screwed up

MY_LAT = 35.689487
MY_LNG = 139.691711
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

data = response.json()
result = data['results']
sunset = result['sunset'].split("T")[1].split(":")[0]
sunrise = result['sunrise'].split("T")[1].split(":")[0]
time_now = datetime.datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
