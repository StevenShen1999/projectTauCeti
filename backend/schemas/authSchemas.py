from schemas import generalSchemas as gs
from marshmallow import Schema, fields, validate, post_load
from models.users import User

class RegistrationSchema(Schema):
    email = gs.email
    username = gs.username
    password = gs.password

    @post_load
    def makeUser(self, data, **kwargs):
        return User(**data)

class LoginSchema(Schema):
    email = gs.email
    password = gs.password