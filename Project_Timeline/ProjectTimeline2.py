import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the Excel file
excel_file = "/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Python_Dev/Timeline.xlsx"
df = pd.read_excel(excel_file)

# Convert date columns to datetime objects
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Sort the DataFrame by End Date in descending order
df = df.sort_values(by='End Date', ascending=False)

# Create a Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the Gantt bars
for index, row in df.iterrows():
    width = (row['End Date'] - row['Start Date']).days  # Calculate the width
    ax.barh(row['Activity'], width, left=row['Start Date'], color='b')

# Format the x-axis as dates in "mm/dd/yy" format with 1-week intervals
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%y"))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)

# Set labels and title
ax.set_xlabel('Timeline')
ax.set_ylabel('Activities (Latest at Bottom)')
plt.title('Gantt Chart')

# Show the Gantt chart
plt.tight_layout()
plt.show()
