import jwt
from datetime import datetime, timedelta
import os
from util.emailServices import sendActivationEmail
from flask import request, abort
from schemas.authSchemas import *
from marshmallow import ValidationError

### Expiration Time For Tokens is 24 Hours
tokenExp = 24*60*60
activationTokenExp = 24*60*60

ADMIN = 'Admin'
USER = 'User'

jwtKey = os.environ.get('TAUCETI_SECRET_KEY')

# Used for token valiation
# A decorator that should be used before API's functions
def validateToken(activation=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not request.headers.get('Authorization'):
                abort(400, "Missing Parametres")

            try:
                token = TokenSchema().load({"token": request.headers.get('Authorization')})
            except ValidationError as e:
                abort(403, "Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")

            try:
                token_data = jwt.decode(
                    token['token'],
                    jwtKey,
                    algorithms='HS256'
                )
            except jwt.DecodeError or jwt.InvalidSignatureError \
                or jwt.ExpiredSignatureError \
                or jwt.ExpiredSignatureError:
                abort(403, "Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")

            return func(token_data=token_data, *args, **kwargs)
        return wrapper
    return decorator

# Handles the generation of an activation token and sending email to the user's email address
# No security checks (assumed all previous security checks have been passed to get to this step)
def registerUser(user):
    # Generate an activcation token
    global activationTokenExp
    token = jwt.encode(
        {
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(seconds=activationTokenExp),
            'email': user.email,
            'type': 'activation'
        },
        jwtKey, algorithm='HS256'
    ).decode('utf-8')

    print(token)
    status = sendActivationEmail(token, user.email)


    return "success" if status == "success" else status

# Handles the generation of a normal token 
# Requires doing security checks
def loginUser(user):
    # Generate a normal token
    global tokenExp
    token = jwt.encode(
        {
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(seconds=tokenExp),
            'email': user.email,
            'type': 'standard'
        },
        jwtKey, algorithm='HS256'
    ).decode('utf-8')

    print(token)
    return token