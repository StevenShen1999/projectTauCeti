from schemas import generalSchemas as gs
from marshmallow import Schema, fields, validate, post_load
from models.messages import Messages
from datetime import datetime
import random
import string
import pytz

class MessageCreationSchema(Schema):
    content = gs.generalerString
    courseID = gs.generalString

    @post_load
    def makeMessage(self, data, **kwargs):
        return Messages(id=''.join(random.choices(string.ascii_letters + string.digits, k=16)),
            content=data['content'], time=pytz.utc.localize(datetime.utcnow()),
            courseid=data['courseID'])

class MessageDeletionSchema(Schema):
    messageID = gs.generalString

class MessagePollingSchema(Schema):
    previousIncrement = gs.generalTimeStamp
    courseID = gs.generalString