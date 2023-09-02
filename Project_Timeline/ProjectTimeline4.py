from flask import Flask, request, render_template
import plotly.figure_factory as ff
from datetime import datetime

app = Flask(__name__)

# List to store activities
activities = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add_activity' in request.form:
            # Add activity to the list
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
        elif 'generate_chart' in request.form:
            # Generate Gantt chart
            gantt_chart = generate_gantt_chart(activities)
            return render_template('index.html', gantt_chart=gantt_chart, activities=activities)

    return render_template('index.html', gantt_chart=None, activities=activities)

def generate_gantt_chart(activities):
    # Create a Gantt chart using Plotly
    df = []

    for activity in activities:
        df.append(dict(Task=activity['activity'],
                        Start=activity['start_date'],
                        Finish=activity['end_date'],
                        Completion_Percentage=activity['completion_percentage'],
                        Status=activity['status']))

    # Collect unique statuses for color mapping
    unique_statuses = set(activity['status'] for activity in activities)

    # Generate colors dynamically for unique statuses
    colors = {status: 'rgb(' + str(hash(status) % 256) + ', ' + str(hash(status) % 256) + ', ' + str(hash(status) % 256) + ')' for status in unique_statuses}

    fig = ff.create_gantt(df, colors=colors, index_col='Status', show_colorbar=True, group_tasks=True)

    # Convert the figure to HTML
    gantt_chart = fig.to_html(full_html=False)

    return gantt_chart

if __name__ == '__main__':
    app.run(debug=True)
