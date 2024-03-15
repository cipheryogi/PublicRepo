import requests

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = 'N5GELYU0NWXTBH77'

# The symbol for Microsoft
symbol = 'MSFT'

# Make a request to Alpha Vantage's Time Series Intraday endpoint
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the latest stock price
    latest_data = data['Time Series (1min)']
    latest_timestamp = list(latest_data.keys())[0]
    latest_price = latest_data[latest_timestamp]['1. open']
    
    print(f"The latest price of {symbol} share is ${latest_price} on {latest_timestamp}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
