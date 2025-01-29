from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'done': True
    }
]

# Define a route for the root URL
@app.route('/')
def home():
    return 'Hello, API!'

if __name__ == '__main__':
    app.run(debug=True)

# Route for retrieving all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route for retrieving a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

if __name__ == '__main__':
    app.run(debug=True)
