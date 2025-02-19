import requests
from datetime import datetime
import  os


current_time = datetime.now()
date_str = current_time.strftime("%Y-%m-%d")
time_str = current_time.strftime("%H:%M:%S")


APP_ID = os.environ["APP_ID"]
API_KEY =os.environ["APP_KEY"]
BEARER = os.environ["BEARER"]

SHEETY_ENDPOINT = "https://api.sheety.co/d32379b2a4647f31d4ac21b3c9916d14/myWorkouts/workouts"


headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

data = {
    "query": input("What exercise did you do today?")
}





response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise",headers=headers, json=data)

end_data = response.json()

print(response.status_code)

exercise_type = end_data["exercises"][0]["name"]
duration = end_data["exercises"][0]["duration_min"]
calories = end_data["exercises"][0]["nf_calories"]

workout_data = {
    "workout":
        {
        "date": date_str,
        "time": time_str,
        "exercise": exercise_type.title(),
        "duration": duration,
        "calories": calories,
        }
}

headers = {
    "Authorization": f"Bearer {BEARER}"
}



sheety_response = requests.post(SHEETY_ENDPOINT, json=workout_data, headers=headers)


