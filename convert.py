print("ellis is awesome")
import requests

API_KEY = "fca_live_X3HHFgkzdN6WqY7QbND0zUVVKZu0i1F2x2UIsFRB"
BASE_URL= f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR" , "COP", "AUD"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    
    except Exception as e:
        print(e)
        return None
    
convert_currency("USD")    