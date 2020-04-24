from namespaces.auth import api
from flask_restplus import fields

registrationDetails = api.model("Registration Details",
    {
        "email": fields.String(required=True),
        "username": fields.String(required=True),
        "password": fields.String(required=True)
    }
)

loginDetails = api.model("Login Details",
    {
        "email": fields.String(required=True),
        "password": fields.String(required=True)
    }
)