from flask import Flask

# initialize the app
app = Flask(__name__)

#Add a route that will handle PUT requests. In this example, let's create a route called 
@app.route('/')
def hello():
    return 'Hello, World! This is a simple API.'

if __name__ == '__main__':
    app.run(debug=True)
