import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/19c8fef61987ddff56f584e28940f963/projectOfFlightDeals/prices"
SHEET_USERS_ENDPOINT = "https://api.sheety.co/19c8fef61987ddff56f584e28940f963/useresPartOfFlightProject/users"



class DataManager:

    def __init__(self):
        # contain the get request with all the data in a dict
        self.destination_data = {}

    def get_sheety_data(self):
        # gets all the requests data and put it in the empty dict
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data_of_sheety = response.json()
        # all the data we need is in the "price" key which is the name of the sheet
        self.destination_data = data_of_sheety["prices"]
        return self.destination_data

    def update_destination_codes(self):
        # for evrey city in the google sheet
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

