import os
import requests

# Get the API key from environment variables
cmc_api_key = os.getenv('API_KEY')

# Base URL for CoinMarketCap API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Parameters for the API call
parameters = {
    'start': '1',  # Starting at the top-ranked coin
    'limit': '10',  # Number of coins to retrieve
    'convert': 'USD'  # Convert prices to USD
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': cmc_api_key,
}

# Make the API request
response = requests.get(url, headers=headers, params=parameters)
data = response.json()

# Print the response or process the data further
print(data)
