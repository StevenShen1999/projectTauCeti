from uuid import uuid4
from datetime import datetime
import pytz

class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.activated = False
        self.points = 0
        self.link = uuid4()
        self.createdat = str(datetime.now(pytz.utc))