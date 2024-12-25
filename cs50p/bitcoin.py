import sys  # For handling command-line arguments
import requests  # For making HTTP requests to retrieve Bitcoin price data

def main():
    try:
        # Check if the correct number of command-line arguments is provided
        if len(sys.argv) != 2:
            sys.exit('Missing command-line argument')  # Exit with an error message if argument is missing

        # Convert the command-line argument to a floating-point number (representing Bitcoin amount)
        bitcoin_nbr = float(sys.argv[1])
    except ValueError:
        # Handle cases where the argument cannot be converted to a number
        print('Command-line argument is not a number')
        exit(1)  # Exit with a non-zero status to indicate an error

    # Fetch the Bitcoin price data from the API
    response = get_response().json()
    
    # Extract the current Bitcoin price in USD from the API response
    current_price = response["bpi"]["USD"]["rate_float"]
    
    # Calculate the total cost for the entered Bitcoin amount
    total_cost = bitcoin_nbr * current_price
    
    # Format the total cost to include commas and four decimal places
    formatted_cost = f"{total_cost:,.4f}"
    
    # Print the entered Bitcoin amount (as an integer for better readability)
    print(f'Your entered bitcoin number is: {int(bitcoin_nbr)}')
    
    # Print the current USD price per Bitcoin with commas for readability
    print(f'Current USD price per bitcoin is: ${current_price:,}')
    
    # Print the total cost of the entered Bitcoin amount in USD
    print(f'Total Cost is: ${formatted_cost}')

def get_response():
    try:
        # Send a GET request to the Coindesk API to fetch the current Bitcoin price
        return requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        # Raise an exception with a custom error message if the request fails
        raise requests.RequestException('Fatal: Error while retrieving data from Coindesk API')

# Entry point of the script
if __name__ == '__main__':
    main()