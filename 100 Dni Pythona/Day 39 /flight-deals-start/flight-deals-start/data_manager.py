import  requests
import  os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()


END_POINT = "https://api.sheety.co/e4367abd397df8e1fb755c731787db28/flightDeals/prices"





class DataManager:
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(END_POINT, auth=self._authorization)
        data = response.json()
        destination_data = data["prices"]
        return destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{END_POINT}/{city['id']}", json=new_data ,auth=self._authorization)
            print(response.text)