from flask import Flask
from flask_cors import CORS
import json
# How to start the server for Flask on windows...
# $ export FLASK_APP=backend.py
# $ export FLASK_DEBUG=1
# $ python -m flask run
# or do this in 1 command
# FLASK_APP=backend.py FLASK_DEBUG=1 python -m flask run

app = Flask(__name__)
CORS(app)

@app.route("/")
# @cross_origin()
def hello():
    return "Hello World!"

@app.route("/get-recommendations")
# @cross_origin()
def recommendations():
    return json.dumps(["1","Donkey","Santa","33","0199212"])
