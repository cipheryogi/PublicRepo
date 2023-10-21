import snowpy
import pyodbc

snowpy.config.USE_PYODBC = True

client = snowpy.Client(instance='myinstance', user='myusername', password='<PASSWORD>')

# Retrieve all incidents
incidents = client.query('incident')

# Print the number  

# snowpy.config.USE_PYODBC = False

# client = snowpy.Client(instance='myinstance', user='myusername', password='mypassword')

# # Retrieve all incidents
# incidents = client.query('incident')

# # Print the number of incidents retrieved
# print(f"Retrieved {len(incidents)} incidents")
