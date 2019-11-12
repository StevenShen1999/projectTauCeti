from flask import request, Flask, send_file, make_response, abort, send_from_directory, Response
from werkzeug.utils import secure_filename
from flask_cors import CORS
import jwt
from functools import wraps
import utilFunc
import utilFuncNotes 
import utilFuncChat
from json import dumps, load
import os
import re

app = Flask(__name__)
UPLOAD_FOLDER = '../database'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png', 'docx', 'jpeg', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['JWT_SECRET_KEY'] = os.urandom(24)

CORS(app)

def allowed_files(filename):
    return True if filename.rsplit(".")[-1] in ALLOWED_EXTENSIONS else False

# Our authorised function will determine if user has logged in with valid credentials
def authorised(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if request.headers['Authorization'] == None:
            payload = {'response': 401, 'msg': "Not logged in"}
            return dumps(payload)

        user = None
        data = request.headers['Authorization'].encode('UTF-8', 'ignore')
        token = str.replace(str(data), 'Bearer ', '')

        try:   
            user = jwt.decode(token, utilFunc.key, algorithms=['HS256'])['sub']
        except:
            return dumps({'response': 400, 'msg': 'Token failed'}), 400
        return f(user, *args, **kws)
    return decorated_function

'''
    App-route for uploading files
    :param: {userID: "", name: "", course: ""}
    Example format:
    files = [
        ('file', (open(r"../database/test1.txt", 'rb'))),
        ('data', ('data', json.dumps(data), 'application/json'))
    ]
    :output: {response: "", msg: ""}
'''
@app.route("/api/uploadFile", methods=['POST'])
def uploadFile():
    if ('file' not in request.files):
        return dumps({'response': 400, "msg": "No file included"}), 400
    data = load(request.files['data'])

    name = data['name']
    course = data['course']
    userID = data['userID']

    if (name == None or course == None or userID == None):
        return dumps({'response': 400, "msg": "Insufficient arguments"}), 400
    elif (utilFunc.checkUserExists(userID) == False):
        return dumps({'response': 400, "msg": "No such user"}), 400

    fileIn = request.files['file']
    if (fileIn.filename == ''):
        return dumps({'response': 400, "msg": "No file included"}), 400
    elif allowed_files(fileIn.filename):
        filename = secure_filename(fileIn.filename)
        fileIn.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        idOutput = utilFuncNotes.saveFile(os.path.join(app.config['UPLOAD_FOLDER'], filename), data['course'], data['name'], data['userID'])
        return dumps({'response': 200, 'msg': idOutput}), 200

'''
    App-route for getting a particular file
    :param: fileID = ?
    :output: {response: "", msg: ""} or just a file
'''
@app.route("/api/downloadFile", methods=['GET'])
def getFile():
    fileID = request.args.get('fileID')
    if (fileID == None):
        return dumps({'response': 400, "msg": "Please specify a file"}), 400
    fileName = utilFuncNotes.getFileName(fileID)
    fileName = fileName.rsplit('/')[-1]
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
    if (error == "user does not exist" or error == "Password incorrect"):
        payload['response'] = 403
        payload['msg'] = error.decode('utf-8')
        return dumps(payload), 403
    else:
        payload['response'] = 200
        payload['msg'] = error.decode('utf-8')
        return dumps(payload), 200

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
        return dumps(payload), 200
    else:
        payload['response'] = 403
        payload['msg'] = output
        return dumps(payload), 403

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

    if (user != userID):
        return dumps({'resposne': 405, 'msg': "Not using the right token"}), 405
    output = utilFunc.logout(userID)
    payload = {}
    if (output != "success"):
        payload['response'] = 405
        payload['msg'] = output
        return dumps(payload), 405
    else:
        payload['response'] = 200
        payload['msg'] = output
        return dumps(payload), 200

'''
    App-route for sending a message
    :param: {'userID': '', 'course': '', 'message': ''}
    :output: {'response': '', 'msg': ''}
'''
@app.route("/api/addChat", methods=['POST'])
def addMessage():
    data = request.get_json()
    if (data == None):
        return dumps({'response': 400, 'msg': 'Not enough arguments'}), 400
    userID = data['userID']
    course = data['course']
    message = data['message']
    if (userID == None or course == None or message == None):
        return dumps({'response': 400, 'msg': 'Not enough arguments'}), 400
    messageID = utilFuncChat.insertChat(message, course, userID)
    return dumps({'response': 200, 'msg': messageID}), 200

'''
    App-route for polling all messages
    :param: course
    :output: {'response': '', 'msg': ''} on success, returns a json-array containing all of the message
    related to the course
'''
@app.route("/api/getChat", methods=['GET'])
def getMessages():
    data = request.args.get('course')
    if (data == None):
        return dumps({'response': 400, 'msg': 'Not enough arguments'}), 400
    return dumps(utilFuncChat.getChat(data)), 200

    return 1

'''
    App-route for deleting a message
    :param: {'messageID': ''}
    :output: {'response': '', 'msg': ''}
'''
@app.route("/api/deleteChat", methods=['POST'])
def deleteMessage():
    data = request.get_json()
    if (data == None):
        return dumps({'response': 400, 'msg': 'Not enough arguments'}), 400
    messageID = data['messageID']
    output = utilFuncChat.removeChat(messageID)
    if (output == 'success'):
        return dumps({'response': '200', 'msg': 'success'}), 200
    else:
        return dumps({'response': '400', 'msg': 'message doesnt exist'}), 400

if __name__ == '__main__':
    app.run()