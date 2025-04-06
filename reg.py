#!/usr/bin/env python

#-----------------------------------------------------------------------
# reg.py
# Authors: Arnold Jiang and Amanda Chan
#-----------------------------------------------------------------------
# imports
import json
import sys
import flask
import database

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

    try:
        # Convert the result from database files as json
        valid, result = database.reg_overviews(query)
        if not valid:
            json_doc = json.dumps([valid, result])
            response = flask.make_response(json_doc)
            response.headers['Content-Type'] = 'application/json'
            return response

        json_doc = json.dumps(result)
        response = flask.make_response(json_doc)
        response.headers['Content-Type'] = 'application/json'
        return response
    except Exception as e:
        print(f"Error in reg_overviews: {str(e)}", file=sys.stderr)
        json_doc = json.dumps([False,
"A server error occurred. Please contact the system administrator."])
        response = flask.make_response(json_doc)
        response.headers['Content-Type'] = 'application/json'
        return response

#-----------------------------------------------------------------------
@app.route('/regdetails', methods=['GET'])
def reg_details():

    query = {"classid": flask.request.args.get("classid")}
    try:
        valid, result = database.reg_details(query)
        if not valid:
            json_doc = json.dumps([valid, result])
            response = flask.make_response(json_doc)
            response.headers['Content-Type'] = 'application/json'
            return response

        json_doc = json.dumps(result)
        response = flask.make_response(json_doc)
        response.headers['Content-Type'] = 'application/json'
        return response

    except Exception:
        json_doc = json.dumps([False,
"A server error occurred. Please contact the system administrator."])
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
