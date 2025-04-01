#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Arnold Jiang and Amanda Chan
#-----------------------------------------------------------------------
# imports
import flask
import database
import json

#-----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return flask.send_file('index.html')

#-----------------------------------------------------------------------
@app.route('/regoverviews', methods=['GET'])
def reg_overviews():
    query = {
        "dept": flask.request.args.get("dept"),
        "coursenum": flask.request.args.get("coursenum"),
        "area": flask.request.args.get("area"),
        "title": flask.request.args.get("title")
    }

    # Convert the result from database files as json
    valid, result = database.reg_overviews(query)
    # ASK QUESTION HERE:
    # The result is not what it is supposed to be for error handling. I would ask about this in OH
    # THIS ISSUE IS PRESENT IN reg_details() too.
    if not valid:
        result = {"error": result}
    
    json_doc = json.dumps(result)
    response = flask.make_response(json_doc)
    response.headers['Content-Type'] = 'application/json'
    return response
    
#-----------------------------------------------------------------------
@app.route('/regdetails', methods=['GET'])
def reg_details():

    query = {"classid": flask.request.args.get("classid")}
    valid, result = database.reg_details(query)
    if not valid:
        result = {"error": result}

    json_doc = json.dumps(result)
    response = flask.make_response(json_doc)
    response.headers['Content-Type'] = 'application/json'
    return response

#-----------------------------------------------------------------------
# For testing:

def _test():
    print(index())
    print()
    print(reg_details())

if __name__ == '__main__':
    _test()
