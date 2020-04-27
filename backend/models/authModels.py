from namespaces.auth import api
from flask_restplus import fields

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
    help="User's email used for registration", location="json")
registrationDetails.add_argument('username', required=True, type=str,
    location="json")
registrationDetails.add_argument('password', required=True, type=str,
    help="8 plus digits, one upper case, one lower, one special character",
    location="json")
'''

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