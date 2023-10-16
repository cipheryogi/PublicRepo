import pandas as pd
from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    percent_complete = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(20))

@app.route('/', methods=['GET'])
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/upload', methods=['POST'])
def upload():
    df = pd.read_excel(request.files['file'], engine='openpyxl')
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['percent_complete'] = df['percent_complete'].astype(float)
    df['status'] = df['status'].str.lower().replace({'not started': 'Not Started', 'on hold': 'On Hold', 'in progress': 'In Progress'})
    df.dropna(subset=['start_date', 'end_date', 'percent_complete', 'status'], inplace=True)
    df.sort_values(['start_date', 'end_date'], ascending=[True, False], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    # Create new database entries for each project
    for i, row in df.iterrows():
        project = Project(id=i+1, start_date=row['start_date'], end_date=row['end_date'], percent_complete=row['percent_complete'], status=row['status'])
        db.session.add(project)
        db.session.commit()
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)