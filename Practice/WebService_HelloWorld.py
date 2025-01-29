# A simple RESTful API in Python 3 using Flask that responds with "Hello, World!" when you access a specific endpoint. (Install flask - PIP INSTALL FLASK)
# This code creates a Flask web application with a single route /hello that responds with "Hello, World!" when accessed using a GET request.

from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Birdie num num!'

if __name__ == '__main__':
    app.run()

# Just execute this code in VS code as VS code will create a webserver to host the webpage. Following is the sample output:
#  Refresher/WebService_HelloWorld.py 
#  * Serving Flask app 'WebService_HelloWorld'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
# Since you see this output, it means our Flask app is running. You can now open a web browser and navigate to http://127.0.0.1:5000/hello to see the "Hello, World!" response from your Flask application.