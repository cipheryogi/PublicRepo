import requests
import os  # For accessing environment variables

# Retrieve API token from environment variable
api_token = os.environ.get("SERVICENOW_API_TOKEN")

# Make sure to set the environment variable SERVICENOW_API_TOKEN with the value of your ServiceNow API token before running the Python script. You can set environment variables in various ways depending on your operating system and environment. Here are a few common methods:
#for MacOS/ Linux the line command is: 
# export SERVICENOW_API_TOKEN='your_api_token_here'
# note that we can set the variable to the token value permanently (until the expiration of the token) in Python as shown below, but that defeats the whole purpose of secure authentication.
# import os
# os.environ["SERVICENOW_API_TOKEN"] = "your_api_token_here"

# Ensure the API token is available
if api_token is None:
    raise ValueError("ServiceNow API token is not provided")

# Define the URL
url = "https://yshinde.service-now.com/api/now/table/incident"

# Set the headers with the API token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_token}"
}

# Make the API request
response = requests.get(url, headers=headers)

# Handle the response
if response.status_code == 200:
    incidents = response.json().get('result')
    print(incidents)
else:
    print(f"Failed to fetch incidents. Status code: {response.status_code}")
