import schemas.generalSchemas as gs
from marshmallow import Schema

class ReportUserSchema(Schema):
    userID = gs.generalString
    reason = gs.generalerString

class UpdateUserSchema(Schema):
    username = gs.generalerNotRequiredString
    email = gs.generalerNotRequiredString