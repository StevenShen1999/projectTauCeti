import schemas.generalSchemas as gs
from marshmallow import Schema, post_load
from uuid import uuid4
from models.courses import Courses
from models.unis import University
from datetime import datetime

class CourseRegistrationSchema(Schema):
    code = gs.course
    name = gs.generalString
    university = gs.generalID
    information = gs.generalerNotRequiredString
    description = gs.generalerNotRequiredString

    @post_load
    def makeCourse(self, data, **kwargs):
        if (not University.query.filter_by(id=data['university']).first()):
            return None
        return Courses(id=str(uuid4().hex), code=data['code'],
            name=data['name'], university=data['university'],
            information=data['information'] if 'information' in data else None,
            description=data['description'] if 'description' in data else None)

class CourseSchema(Schema):
    id = gs.generalString

class CoursePatchSchema(Schema):
    id = gs.generalString
    name = gs.generalerNotRequiredString
    information = gs.generalerNotRequiredString

class CourseDescSchema(Schema):
    id = gs.generalString
    description = gs.generalerString

class CourseReportSchema(Schema):
    courseID = gs.generalString
    reason = gs.generalString

class CourseChangelogSchema(Schema):
    id = gs.generalString

class CourseUserSchema(Schema):
    id = gs.generalerNotRequiredString