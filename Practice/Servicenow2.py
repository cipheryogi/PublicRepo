import requests
import openpyxl

url = "https://demotechnologywf38425.service-now.com/api/now/table/incident"
response = requests.get(url, auth=("admin", "password!"))

if response.status_code == 200:
    incidents = response.json().get("result")
    print("Incidents:", incidents)  # Add this line to check the structure
    
    # Create a new Excel workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Write headers
    sheet["A1"] = "Incident Number"
    sheet["B1"] = "Short Description"
    
    # Write incident data to Excel
    row = 2  # Start from row 2 to skip header row
    for incident in incidents[:10]:  # Loop through only the first 10 records
        if isinstance(incident, dict):  # Check if incident is a dictionary
            sheet[f"A{row}"] = incident.get('number', 'N/A')  # Use .get() to handle missing keys
            sheet[f"B{row}"] = incident.get('short_description', 'N/A')
        else:
            print(f"Skipping invalid incident data: {incident}")
        row += 1
    
    # Save the workbook
    workbook.save("incidents.xlsx")
