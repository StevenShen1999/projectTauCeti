from flask import request, Flask, send_file, make_response, abort
from flask_cors import CORS
import jwt
from functools import wraps
from utilFunc import key
import utilFunc
from json import dumps
import os

app = Flask(__name__)
CORS(app)

# Our authorised function will determine if user has logged in with valid credentials
def authorised(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'Authorization' in request.headers:
            payload = {'response': 401, 'msg': "Not logged in"}
            return dumps(payload)

        user = None
        data = request.headers['Authorization'].encode('ascii','ignore') 
        token = str.replace(str(data), 'Bearer ', '')
        try:
            user = jwt.decode(token, key, algorithms=['HS256'])['sub']
        except:
            payload = {'response': 401, 'msg': "Not logged in"}
            return dumps(payload)
        return f(user, *args, **kws)
    return decorated_function

'''
    App-route for logging in a user
    :param: {userID: "", password: ""}
    :output: {"response": "", msg: ""}
    Output provides error message on errors, otherwise msg includes the token
'''
@app.route("/api/login", methods=['POST'])
def login():
    data = request.get_json()
    userID = data['userID']
    password = data['password']

    error = utilFunc.login(userID, password)
    payload = {}
    if (isinstance(error, str)):
        payload['response'] = 403
        payload['msg'] = error
    else:
        payload['response'] = 200
        payload['msg'] = error
        print(payload)
    return dumps(payload)

'''
    App-route for registering a user
    :param: {userID: "", password; ""}
    :output: {response: "", msg: ""}
    Output provides error message on errors, otherwise msg is not incldued
'''
@app.route("/api/register", methods=['POST'])
def register():
    data = request.get_json()
    userID = data['userID']
    password = data['password']

    output = utilFunc.createUser(userID, password)
    payload = {}
    if (payload != "success"):
        payload['response'] = 200
    else:
        payload['response'] = 403
        payload['msg'] = output
    return dumps(payload)

'''
    App-route for logging out
    :param: {userID: ""}
    :output: {resposne: "", msg: ""}
'''
@app.route("/api/logout", methods=['GET'])
@authorised
def logout(user):
    data = request.get_json()
    userID = data['userID']

    output = utilFunc.logout(userID)
    payload = {}
    if (payload != "success"):
        payload['response'] = 405
        payload['msg'] = output
    else:
        payload['response'] = 200
        payload['msg'] = output
    return dumps(payload)

if __name__ == '__main__':
    app.run()