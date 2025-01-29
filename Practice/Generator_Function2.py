import pandas as pd

def read_excel_rows_generator(excel_file_path):
    # Open the Excel file using ExcelFile
    excel_file = pd.ExcelFile(excel_file_path)

    # Get the sheet names from the Excel file
    sheet_names = excel_file.sheet_names

    # Loop through each sheet
    for sheet_name in sheet_names:
        # Read the current sheet into a DataFrame
        df = excel_file.parse(sheet_name)
        
        # Process the rows in the DataFrame
        for index, row in df.iterrows():
            # Yield each row as a generator item
            yield row

    # Close the Excel file when done (optional)
    excel_file.close()


excel_file_path = '/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Dev_Public/Project_Timeline/Timeline.xlsx'
for row in read_excel_rows_generator(excel_file_path):
    # Process each row here
    print(row)

    d = {}
    d.values
