import requests
import openpyxl

# url = "https://demotechnologywf38425.service-now.com/api/now/table/incident"
url = "https://yshinde.service-now.com/api/now/table/incident"
response = requests.get(url, auth=("admin", "password!"))

incidents = response.json().get('result')
print(incidents)
