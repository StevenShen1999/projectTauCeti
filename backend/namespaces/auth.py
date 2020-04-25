from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with

api = Namespace("auth", description="APIs to handle authentication related queries")

from models.users import Users
from app import db
from models.authModels import *
from schemas.authSchemas import *
from util.authServices import registerUser, validateToken, loginUser
from flask import jsonify
from hashlib import sha256

@api.route("/register")
class Register(Resource):
    @api.response(200, "Sucess")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Credentials (Email or Username Taken)")
    @api.response(409, "Account with this email address already exists")
    @api.response(500, "Email service not currently avaliable, sending email not successful")
    @api.expect(registrationDetails)
    @api.doc(description='''
        Registering an account with the given parametre, note: password must be longer than 8 characters,
        contains an upper case character, a lower case character and also a special character
    ''')
    @validate_with(RegistrationSchema)
    def post(self, data):
        exists = Users.query.filter_by(email=data.email).first()
        if exists: abort(409, "Account with this email address already exists")

        db.session.add(data)
        db.session.commit()

        status = registerUser(data)

        if status != "success":
            abort(500, "Email service not currently avaliable, sending email not successful")
        return jsonify({"message": "Success"})

@api.route("/activate")
class Activate(Resource):
    @api.response(200, "{'message': 'Success'}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")
    @api.response(409, "Account Already Activated")
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to activate accounts, requires the JWT sent to users' email. Note: no request body needed")
    @validateToken()
    def post(self, token_data):
        if token_data['type'] != "activation":
            abort("Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")

        userEmail = token_data['email']
        user = Users.query.filter_by(email=userEmail).first()
        if not user: abort(403, "User Not Found")

        if user.activated == True: abort(409, "Account Already Activated")
        user.activated = True
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Success"})

@api.route("/login")
class Login(Resource):
    @api.response(200, "{'message': 'success', 'token': 'someJWTString'}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Credentials (Wrong Email or Password)")
    @api.response(405, "This account isn't activated, please activate your account")
    @api.expect(loginDetails)
    @api.doc(description="API For Logging In Users")
    @validate_with(LoginSchema)
    def post(self, data):
        user = Users.query.filter_by(email=data['email'], 
            password=sha256(data['password'].encode('UTF-8')).hexdigest()).first()

        if not user: abort(403, "Invalid Credentials (Wrong Email Or Password)")
        elif user.activated == False: abort(405, "This account isn't activated, please activate your account")

        token = loginUser(user)
        return jsonify({"message": "Success", "token": token})

@api.route("/lost")
class Lost(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Credentials (Wrong Email or Password)")
    @api.response(409, "Account Already Activated")
    @api.response(500, "Email service not currently avaliable, sending email not successful")
    @api.expect(loginDetails)
    @api.doc(description='''
        This API is designed for people who didn't receive an activation email\
            or those who didn't activate their account and cbf to find the activation email
    ''')
    @validate_with(LoginSchema)
    def post(self, data):
        user = Users.query.filter_by(email=data['email'], 
            password=sha256(data['password'].encode('utf-8')).hexdigest()).first()

        if not user: abort(403, "Invalid Credentials (Wrong Email or Password)")
        elif user.activated == True: abort(409, "Account Already Activated")

        emailStatus = registerUser(user)
        if emailStatus != "success": abort(500, "Email service not currently avaliable, sending email not successful")

        return jsonify({"message": "Success"})

# Stub API
"""
@api.route("/forgot")
class Forgot(Resource):
    @api.doc(description='''API Not Implemented''')
    def post(self):
        # TODO: TO BE COMPLETED, SECONDARY IMPORTANT ROUTE
        return 0
"""