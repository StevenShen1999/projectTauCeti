from flask_restplus import Resource, abort, Namespace
from util.validation import validate_with

api = Namespace("auth", description="APIs to handle authentication related queries")

from models.authModels import *
from schemas.authSchemas import *

@api.route("/register")
class Register(Resource):
    @api.response(400, "Missing Email/Username/Password")
    @api.response(403, "Invalid Credentials (Email or Username Taken)")
    @api.expect(registrationDetails)
    @api.doc(description='''
        Registering an account with the given parametre, note: password must be longer than 8 characters,
        contains an upper case character, a lower case character and also a special character
    ''')
    @validate_with(RegistrationSchema)
    def post(self, data):
        print(data)
        return "Success"

@api.route("/login")
class Login(Resource):
    @api.response(400, "Missing Email/Password")
    @api.response(403, "Invalid Credentials (Wrong Email or Password)")
    @api.expect(loginDetails)
    def post(self):
        return "success"