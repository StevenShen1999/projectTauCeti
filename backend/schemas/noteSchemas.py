from schemas import generalSchemas as gs
from marshmallow import Schema, fields, validate, post_load
from models.notes import Notes
from datetime import datetime
from uuid import uuid4

class creationSchema(Schema):
    courseID = gs.generalString
    name = gs.generalString
    price = gs.generalInteger

    @post_load()
    def makeNote(self, data, **kwargs):
        return Notes(id=str(uuid4().hex), courseid=data['courseID'], points=0,
            price=data['price'] if 'price' in data else 0,
            uploadtime=str(datetime.utcnow()), name=data['name'])

class notesGeneralSchema(Schema):
    noteID = gs.generalString

class courseNoteSchema(Schema):
    courseCode = gs.course

class noteVoterSchema(Schema):
    noteID = gs.generalString
    vote = gs.generalInteger

class noteReportSchema(Schema):
    noteID = gs.generalString
    reason = gs.generalerString