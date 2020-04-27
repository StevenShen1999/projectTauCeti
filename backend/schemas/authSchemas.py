from schemas import generalSchemas as gs
from marshmallow import Schema, fields, validate, post_load
from models.users import Users
from datetime import datetime
import pytz
import random
from string import ascii_letters, digits
from hashlib import sha256

class RegistrationSchema(Schema):
    email = gs.email
    username = gs.username
    password = gs.password

    @post_load
    def makeUser(self, data, **kwargs):
        # Defaults to creating a user of permission level 0 (i.e. normal user)
        return Users(email=data['email'], username=data['username'], 
            password=sha256(data['password'].encode('UTF-8')).hexdigest(),
            activated=False, points=0,
            link=''.join(random.choices(ascii_letters + digits, k=16)), 
            createddate=str(datetime.utcnow()), role=0, failedlogins=0)

class LoginSchema(Schema):
    email = gs.email
    password = gs.password

class VerificationSchema(Schema):
    email = gs.email
    password = gs.password
    verification = gs.generalInteger

class TokenSchema(Schema):
    token = gs.token