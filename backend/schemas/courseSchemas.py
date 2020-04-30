import schemas.generalSchemas as gs
from marshmallow import Schema, post_load
from uuid import uuid4
from models.courses import Courses

class CourseRegistrationSchema(Schema):
    code = gs.course
    name = gs.generalString
    university = gs.generalString
    information = gs.generalerNotRequiredString

    @post_load
    def makeCourse(self, data, **kwargs):
        return Courses(id=str(uuid4().hex), code=data['code'],
            name=data['name'], university=data['university'],
            information=data['information'] if 'information' in data else None)

class CourseSchema(Schema):
    id = gs.generalString

class CoursePatchSchema(Schema):
    id = gs.generalString
    name = gs.generalerNotRequiredString
    information = gs.generalerNotRequiredString