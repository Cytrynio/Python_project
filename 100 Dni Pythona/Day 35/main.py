import  requests
import os
from twilio.rest import Client



account_sid = "ACe1bddcb8b1b001e5693d1575bafef782"
auth_token = os.environ.get("AUTH_TOKEN")
weather_app_api_key = os.environ.get("OMW_API_KEY")


weather_params = {
    "lat": 18.6464,
    "lon": 4.3521,
    "appid": weather_app_api_key,
    "cnt":4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)

response.raise_for_status()
status_code=response.status_code

data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_="+18573418987",
        to="+48692313074",
    )
    print(message.status)



