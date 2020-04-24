from namespaces.courses import api
from flask_restplus import fields

courseCreationDetails = api.model("Course Creation Details",
    {
        "code": fields.String(required=True),
        "name": fields.String(required=True),
        "semester": fields.String(required=True),
        "university": fields.String(required=True)
    }
)

courseDetails = api.model("For APIs requiring to get info about a course",
    {
        "id": fields.String(required=True)
    }
)