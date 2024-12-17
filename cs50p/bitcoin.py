import sys
import requests

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit('Missing command-line argument')
        bitcoin_nbr = float(sys.argv[1])
    except ValueError:
        print('Command-line argument is not a number')
        exit(1)

    response = get_response().json()
    current_price = response["bpi"]["USD"]["rate_float"]
    total_cost = bitcoin_nbr * current_price
    formatted_cost = f"{total_cost:,.4f}"
    print(f'Your entered bitcoin number is: {int(bitcoin_nbr)}')
    print(f'Current USD price per bitcoin is: ${current_price:,}')
    print(f'Total Cost is: ${formatted_cost}')

def get_response():
    try:
        return requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        raise requests.RequestException('Fatal: Error while retriving data from itune API')

if __name__=='__main__':
    main()