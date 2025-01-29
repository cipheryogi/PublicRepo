from flask import Flask, jsonify

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return 'Hello, World!'

# Define a route for the /api endpoint
@app.route('/api')
def api():
    return jsonify({'message': 'Welcome to the API!'})

if __name__ == '__main__':
    app.run(debug=True)
