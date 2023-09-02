from flask import Flask, request, render_template
import plotly.figure_factory as ff
from datetime import datetime

app = Flask(__name__)

# Sample data structure to store activities
activities = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process user input and store in the activities list
        activity = request.form['activity']
        status = request.form['status']
        completion_percentage = int(request.form['completion_percentage'])
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

        activities.append({
            'activity': activity,
            'status': status,
            'completion_percentage': completion_percentage,
            'start_date': start_date,
            'end_date': end_date
        })

        # Generate Gantt chart
        gantt_chart = generate_gantt_chart(activities)

        return render_template('index.html', gantt_chart=gantt_chart)

    return render_template('index.html', gantt_chart=None)

def generate_gantt_chart(activities):
    # Create a Gantt chart using Plotly
    df = []

    for activity in activities:
        df.append(dict(Task=activity['activity'],
                        Start=activity['start_date'],
                        Finish=activity['end_date'],
                        Completion_Percentage=activity['completion_percentage'],
                        Status=activity['status']))

    # Dynamically generate the colors dictionary based on unique statuses
    unique_statuses = set(activity['status'] for activity in activities)
    colors = {status: f'rgb({r}, {g}, {b})' for status, r, g, b in zip(unique_statuses, range(0, 256, 256 // len(unique_statuses)), range(128, 256, 256 // len(unique_statuses)), range(0, 256, 256 // len(unique_statuses)))}

    fig = ff.create_gantt(df, colors=colors, index_col='Status', show_colorbar=True, group_tasks=True)

    # Convert the figure to HTML
    gantt_chart = fig.to_html(full_html=False)

    return gantt_chart

if __name__ == '__main__':
    app.run(debug=True)
