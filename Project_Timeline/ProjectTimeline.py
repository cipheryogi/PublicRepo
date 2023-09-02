from flask import Flask

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import random


app = Flask(__name__)

# Initialize Matplotlib in the main thread
plt.figure(figsize=(10, 6))
plt.xlabel('Calendar dates')
plt.ylabel('Activities')
plt.title('Activity timeline')

def load_excel_data(filepath):
    df = pd.read_excel(filepath)
    return df

def generate_timeline_chart(data):
    # logic to draw the chart.

# # Sample Excel data (replace with your actual data)
#     data = {
#         'Activity name': ['Task A', 'Task B', 'Task C'],
#         'Start date': ['2023-09-01', '2023-09-02', '2023-09-03'],
#         'End date': ['2023-09-04', '2023-09-05', '2023-09-06'],
#         '% Complete': [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
#         'Status': ['In Progress', 'Blocked', 'Completed']
#     }

#     # Convert dates to datetime objects
#     data['Start date'] = pd.to_datetime(data['Start date'])
#     data['End date'] = pd.to_datetime(data['End date'])

#     # Define the 10-day date range
#     start_date = min(data['Start date'])
#     end_date = start_date + datetime.timedelta(days=10)

#     # Create a figure and axis
#     fig, ax = plt.subplots(figsize=(10, 8))

#     # Create a horizontal bar chart (Gantt chart) with activity names on the y-axis
#     for i, activity in enumerate(data['Activity name']):
#         ax.barh(activity, width=data['End date'][i] - data['Start date'][i], left=data['Start date'][i], label=activity)
#         # Display % Complete and Status as annotations on the bars
#         ax.annotate(f'% Complete: {data["% Complete"][i]}%\nStatus: {data["Status"][i]}',
#                     xy=(data['Start date'][i], i), xytext=(5, 7), textcoords='offset points')

#     # Set y-axis label and title for the main subplot
#     ax.set_ylabel('Activity Names')
#     ax.set_title('Activity Timeline')

#     # Add date headers at the top of the chart with the desired format
#     ax2 = ax.secondary_xaxis('top')
#     ax2.set_xlabel('Calendar Dates')

#     # Define the date_ticks variable with the date range
#     date_ticks = pd.date_range(start=start_date, end=end_date)

#     # Set x-axis ticks and labels for the secondary x-axis
#     ax2.set_xticks(date_ticks)
#     ax2.set_xticklabels(date_ticks.strftime('%Y-%m-%d'), rotation=45)

#     # Remove the bottom x-axis
#     ax.xaxis.set_visible(False)

# plot logic end

    # Display the chart
    plt.legend()
    plt.tight_layout()
    plt.show()
    # Save the chart as an image
    plt.savefig('timeline_chart.png')

Excelfile = "/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Python_Dev/Timeline.xlsx"

@app.route('/timeline')
def generate_timeline():
    try:
        excel_data = load_excel_data(Excelfile)
        generate_timeline_chart(excel_data)
        return 'Timeline chart generated'
    except Exception as e:
        print(f'Error occurred: {str(e)}')
        return 'Error occurred'

if __name__ == '__main__':
    app.run(debug=True)


