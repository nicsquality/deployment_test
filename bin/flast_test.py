import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def addition():
    return 'Sum of 2 and 3 is: {}'.format(2 + 3)

app.run(host='0.0.0.0', port=80)