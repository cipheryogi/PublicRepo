import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import xlsxwriter
import os

# Read the input Excel file
input_file = 'input_tasks.xlsx'
if not os.path.exists(input_file):
    raise FileNotFoundError(f"The input file '{input_file}' was not found.")

df = pd.read_excel(input_file)

# Ensure the columns are stripped of any leading or trailing spaces
df.columns = df.columns.str.strip()

# Print column names to verify
print("Column names:", df.columns)

# Convert dates to datetime objects
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Create a figure and axis for the timeline chart
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate the position of each task on the y-axis
y_pos = range(len(df))

# Plot the bars for the timeline with rounded edges
for i, row in df.iterrows():
    # Calculate the full length of the bar (total duration of the task)
    full_length = (row['End Date'] - row['Start Date']).days
    
    # Plot the full task duration bar (light color) with rounded edges
    ax.barh(i, full_length, left=row['Start Date'], color='lightblue', edgecolor='black', height=0.4, linewidth=1, zorder=2)
    
    # Plot the % complete part of the bar (dark color) with rounded edges
    completed_length = full_length * row['% Complete'] / 100
    ax.barh(i, completed_length, left=row['Start Date'], color='darkblue', edgecolor='black', height=0.3, linewidth=1, zorder=3)
    
    # Annotate the % Complete on the darker bar
    ax.text(row['Start Date'] + pd.Timedelta(days=completed_length) + pd.Timedelta(days=1), 
            i, f"{row['% Complete']}%", va='center', color='white', fontsize=9, weight='bold')

# Format the x-axis to show both weeks and months
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Add a secondary x-axis for months at the top
ax_secondary = ax.twiny()
ax_secondary.xaxis.set_major_locator(mdates.MonthLocator())
ax_secondary.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax_secondary.set_xlim(ax.get_xlim())
ax_secondary.xaxis.tick_top()

# Invert y-axis to have the first task on top
plt.gca().invert_yaxis()

# Set the y-axis labels for tasks
ax.set_yticks(y_pos)
ax.set_yticklabels(df['Task Description'])

# Add a grid for clarity
ax.grid(True)

# Set axis labels
ax.set_xlabel('Timeline')
ax.set_ylabel('Tasks')

# Set the title of the chart
ax.set_title('Task Timeline Chart')

# Save the figure as an image instead of showing it
timeline_image = 'timeline_chart.png'
fig.savefig(timeline_image, dpi=300, bbox_inches='tight')
print(f"Timeline chart saved as '{timeline_image}'.")

# Write the DataFrame to a new Excel file and include the timeline chart
output_file = 'output_tasks.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Tasks', index=False)
    
    # Add the timeline chart to the Excel file
    workbook = writer.book
    worksheet = writer.sheets['Tasks']
    worksheet.insert_image('H2', timeline_image)

print(f"Output file '{output_file}' created successfully.")