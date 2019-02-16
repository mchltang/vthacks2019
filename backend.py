from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
# @cross_origin()
def hello():
    return "Hello World!"

@app.route("/get-recommendations")
# @cross_origin()
def recommendations():
    return json.dumps("Best Recommendation Here")
