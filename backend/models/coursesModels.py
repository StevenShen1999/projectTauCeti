from namespaces.courses import api
from flask_restplus import fields

courseCreationDetails = api.model("Course Creation Details",
    {
        "code": fields.String(required=True, example="COMP1911"),
        "name": fields.String(required=True, example="Introduction To Computing A"),
        "semester": fields.String(required=True, example="[0-9][0-9][tTsS][0-4] (i.e. 19T2)"),
        "university": fields.String(required=True, example="University of New South Wales")
    }
)

courseDetails = api.model("For APIs requiring to get information about a course",
    {
        "id": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852")
    }
)