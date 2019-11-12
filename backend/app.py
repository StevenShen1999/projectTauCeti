from flask import request, Flask, send_file, make_response
from flask_cors import CORS
import jwt
from functools import wraps
import utilFunc
from json import dumps

app = Flask(__name__)
CORS(app)

# Our authorised function will determine if user has logged in with valid credentials
def authorised(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        # Handle Authentication
        # Make query to database

        # TODO
        return f(*args, **kws)
    return decorated_function

'''
    App-route for logging in a user
    :param: {userID: "", password: ""}
    :output: {"response": "", msg: ""}
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
        return dumps(payload)
    else:
        payload['response'] = 200
        return dumps(payload)

if __name__ == '__main__':
    app.run()