from namespaces.auth import api
from flask_restplus import fields
from werkzeug import FileStorage

'''
registrationDetails = api.model("Registration Details",
    {
        "email": fields.String(required=True, example="something@somemail.com"),
        "username": fields.String(required=True, example="junyangSim"),
        "password": fields.String(required=True, example="Abcd1234@")
    }
)
'''

registrationDetails = api.parser()
registrationDetails.add_argument('email', required=True, type=str,
    help="User's email used for registration", location="form")
registrationDetails.add_argument('username', required=True, type=str,
    help="Username could be anything under 255 characters", location="form")
registrationDetails.add_argument('password', required=True, type=str,
    help="8 plus digits, one upper case, one lower, one special character",
    location="form")
registrationDetails.add_argument('profilePicture', required=False, type=FileStorage,
    help="User's intended profile picture to be uploaded", location="files")

loginDetails = api.model("Login Details",
    {
        "email": fields.String(required=True, example="something@somemail.com"),
        "password": fields.String(required=True, example="Abcd1234@")
    }
)

verifyDetails = api.model("For verifying accounts",
    {
        "email": fields.String(required=True, example="something@somemail.com"),
        "password": fields.String(required=True, example="Abcd1234@"),
        "verification": fields.String(required=True, example="833123")
    }
)

changePasswordDetails = api.model("For changing a user's password",
    {
        "oldPassword": fields.String(required=True, example="Abcd1234@"),
        "newPassword": fields.String(required=True, example="Aedf4321@")
    }
)