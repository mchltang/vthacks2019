from flask import Flask
from flask_cors import CORS
from flask import request
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

@app.route("/getAnimeList")
def getAnimeList():
    return json.dumps(["1","Donkey","Santa","33","0199212"])


@app.route("/get-recommendations")
# @cross_origin()
def getRecommendations():
    # http://10.1.1.1:5000/login?username=alex&password=pw1
    animeName = request.args.get('anime');
    showRating = request.args.get('score');
    showType = request.args.get('medium');
    showStatus = request.args.get('status');
    # genreBlacklist = request.args.get('blacklist');
    #return MichaelMagicMethod();
    return json.dumps(["1","Donkey","Santa","33","0199212"])
