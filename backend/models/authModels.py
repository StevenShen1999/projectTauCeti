from namespaces.auth import api
from flask_restplus import fields

registrationDetails = api.model("Registration Details",
    {
        "email": fields.String(),
        "username": fields.String(),
        "password": fields.String()
    }
)

loginDetails = api.model("Login Details",
    {
        "email": fields.String(),
        "password": fields.String()
    }
)