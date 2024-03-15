import requests
import openpyxl

# url = "https://demotechnologywf38425.service-now.com/api/now/table/incident"
url = "https://yshinde.service-now.com/api/now/table/incident"
response = requests.get(url, auth=("admin", "Yogi4091!"))
try:
    if response.status_code == 200:
        incidents = response.json().get("result")
        for incident in incidents:
            print(f"Incident {incident['number']}: {incident['short_description']}")
    else:
        print('Error: Could not connect to instance',response.status_code)
except requests.exceptions.HTTPError as e:
    print(f'Error: {e}')
