import  requests
import os


TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):

    if data is None or not data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price,origin,destination,out_date,return_date)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight


    # def __init__(self):
    #     self._api_key = os.environ["AMADEUS_API_KEY"]
    #     self._api_secret = os.environ["AMADEUS_API_SECRET"]
    #     self._token = self.get_new_token()
    #
    # def get_new_token(self):
    #     header = {
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     body = {
    #         'grant_type': 'client_credentials',
    #         'client_id': self._api_key,
    #         'client_secret': self._api_secret
    #     }
    #     response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
    #
    #     print(f"Your token is {response.json()['access_token']}")
    #     print(f"Your token expires in {response.json()['expires_in']} seconds")
    #     return response.json()['access_token']
