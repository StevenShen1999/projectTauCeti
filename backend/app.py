from flask import request, Flask, send_file, make_response, abort, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
import jwt
from functools import wraps
from utilFunc import key
import utilFunc
import utilFuncNotes 
from json import dumps
import os

app = Flask(__name__)
UPLOAD_FOLDER = '../database'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png', 'docx', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

CORS(app)

def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    App-route for uploading files
    :param: {userID: "", name: "", course: "", file}
    :output: {response: "", msg: ""}
'''
@app.route("/api/uploadFile", methods=['POST'])
def uploadFile():
    if ('file' not in request.files):
        return dumps({'response': 400, "msg": "No file included"})
    fileIn = request.files['file']
    if (fileIn.filename == ''):
        return dumps({'response': 400, "msg": "No file included"})
    elif allowed_files(fileIn.filename):
        filename = secure_filename(fileIn.filename)
        fileIn.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        utilFuncNotes.saveFile(os.path.join(app.config['UPLOAD_FOLDER'], filename), request.get_json['userID'])

'''
    App-route for getting a particular file
    :param: {fileID: ""}
    :output: {response: "", msg: ""} or just a file
'''
@app.route("/api/downloadFile", methods=['GET'])
def getFile():
    data = request.get_json()
    if (data['fileID'] == None):
        return dumps({'response': 400, "msg": "Please specify a file"})
    fileName = utilFuncNotes.getFileName(data['fileID'])
    return send_from_directory(app.config['UPLOAD_FOLDER'], fileName)

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