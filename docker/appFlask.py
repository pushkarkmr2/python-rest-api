#!flask/bin/python
from flask import Flask, jsonify


app = Flask(__name__)

# Hello world endpoint
@app.route('/')
def hello():
    return 'Hello world!'

# Verify the status of the microservice
@app.route('/health')
def health1():
    return '{ "status" : "UP" }'

# Get environment details
@app.route('/env')
def data():
    data = {
        'username': 'PythonFlask',
        'message': 'Hello From Python using Flask.'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)