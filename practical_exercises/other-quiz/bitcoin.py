import sys
from requests import request, get, RequestException

def price_checker(given_currency):
# Creating the function to fetch the current price of Bitcoin in the 
# specified given_currency from the CoinDesk API.

    link = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = get(link)
        response.raise_for_status()
        data = response.json()
        if given_currency not in data["bpi"]:
            return None
        return data["bpi"][given_currency]["rate_float"]
    except RequestException as error:
        print(f"Error while fetching data from API: {error}")
        sys.exit(1)

# ---------------- The main function of the whole program ------------------------

if len(sys.argv) != 3:
    sys.exit("You're expected to use: python script.py <number of Bitcoins> <currency (GBP, USD, EUR)>")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Fatal: The first argument must be a number representing the number of Bitcoins.")

given_currency = sys.argv[2].upper()
accepted_currency = ["GBP", "USD", "EUR"]

if given_currency not in accepted_currency:
    sys.exit("Fatal: The expected currencies are GBP, USD, or EUR.")

price = price_checker(given_currency)
if price is None:
    sys.exit(f"Fatal: Not able to fetch price for given currency {given_currency}.")

total_cost = bitcoins * price
formatted_cost = f"{total_cost:,.4f}"
print(f"The current cost of {bitcoins} Bitcoins in {given_currency} is {formatted_cost} {given_currency}.")