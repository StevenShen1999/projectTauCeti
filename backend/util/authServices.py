import jwt
from datetime import datetime
import os

### Expiration Time For Tokens is 60 Minutes
token_exp = 60*60
activationToken_exp = 24*60*60

ADMIN = 'Admin'
USER = 'User'

jwtKey = os.environ.get('TAUCETI_SECRET_KEY')


## TODO: Complete a login function to send JWTs