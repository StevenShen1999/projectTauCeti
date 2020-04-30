import jwt
from datetime import datetime, timedelta
import os
from util.emailServices import sendActivationEmail, sendVerificationEmail
from flask import request, abort
from schemas.authSchemas import *
from marshmallow import ValidationError
from models.users import Users
from random import Random
import string
from app import db

### Expiration Time For Tokens is 24 Hours
tokenExp = 24*60*60
activationTokenExp = 24*60*60

ADMIN = 'Admin'
USER = 'User'

jwtKey = os.environ.get('TAUCETI_SECRET_KEY')

# Used for token valiation
# A decorator that should be used before API's functions
def validateToken(activation=True, roleRequired=0):
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
            except jwt.PyJWTError:
                abort(403, "Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")

            exists = Users.query.filter_by(email=token_data['email']).first()
            if not exists:
                abort(403, "Invalid Token (Most Likely Token's Secret Not Valid Or Expired Token)")
            elif exists.role < roleRequired:
                abort(403, "Account doesn't have enough permission, admin required")
            elif exists.lockeduntil and exists.lockeduntil > datetime.utcnow():
                abort(425, "Account locked, please try again in 24 hours")

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
            'id': user.id,
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
def loginUser(user, data):
    # Generate a normal token
    if not user:
        abort(403, "Invalid Credentials (Wrong Email Or Password)")
    elif user.lastloggedin:
        if(datetime.utcnow().date() - user.lastloggedin.date()).days > 31:
            status = generateVerification(user)
            if status != "success": abort(500, "Email service not currently avaliable, sending email not successful")
            else: abort(423, "More than 31 days since last login, a verification code sent to email, use that to verify at POST /auth/verify")
    elif user.password != sha256(data['password'].encode('UTF-8')).hexdigest():
        if (user.failedlogins >= 5):
            user.lockeduntil = datetime.utcnow() + timedelta(days=1)
            db.session.add(user)
            db.session.commit()
            abort(412, "Account locked, please try again in 24 hours")
        user.failedlogins += 1
        db.session.add(user)
        db.session.commit()
        abort(403, "Invalid Credentials (Wrong Email or Password)")
    elif user.activated == False:
        abort(405, "This account isn't activated, please activate your account")
    elif user.lockeduntil:
        if user.lockeduntil > datetime.utcnow(): abort(412, "Account locked, please try again in 24 hours")
        else: user.lockeduntil = None

    user.lastloggedin = datetime.utcnow().date()
    user.failedlogins = 0

    global tokenExp
    token = jwt.encode(
        {
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(seconds=tokenExp),
            'id': user.id,
            'email': user.email,
            'permission': user.role,
            'type': 'standard'
        },
        jwtKey, algorithm='HS256'
    ).decode('utf-8')

    print(token)
    db.session.add(user)
    db.session.commit()
    return token

def verifyUser(user, data):
    if not user.verificationcode:
        abort(409, "Account already verified, verification code expired")
    elif str(user.verificationcode) != str(data['verification']):
        abort(403, "Invalid Credentials (wrong verification code)")

    user.verificationcode = None
    user.lastloggedin = datetime.utcnow()
    db.session.add(user)
    db.session.commit()

    return loginUser(user, data)


def generateVerification(user):
    # Sets user's verification code to a random 6 lengthed integer
    # Send that verification code to the user's email
    code = ''.join(Random().choices(string.digits, k=6))
    user.verificationcode = code

    db.session.add(user)
    db.session.commit()

    status = sendVerificationEmail(code, user.email)

    return "success" if status == "success" else status