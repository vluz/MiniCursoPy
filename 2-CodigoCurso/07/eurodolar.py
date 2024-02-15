import requests
from pprint import pprint


response = requests.get("https://open.er-api.com/v6/latest/EUR")
# pprint(response.json())
print("\n\nUm Euro vale " + str(response.json()['rates']['USD']) + " Dólares.")