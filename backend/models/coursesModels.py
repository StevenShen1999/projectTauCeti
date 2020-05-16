from namespaces.courses import api
from flask_restplus import fields

courseCreationDetails = api.model("Course Creation Details",
    {
        "code": fields.String(required=True, example="COMP1911"),
        "name": fields.String(required=True, example="Introduction To Computing A"),
        "university": fields.String(required=True, example="University of New South Wales"),
        "information": fields.String(required=False, example="Pretty good course for the normies (A quick overview for the course)"),
        "description": fields.String(required=False, example="Some kind of markdown (Open for edits from everyone)")
    }
)

courseDetails = api.model("For APIs requiring to get information about a course",
    {
        "id": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852")
    }
)

coursePatchDetails = api.model("For APIs to update information about a course",
    {
        "id": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852"),
        "name": fields.String(required=False, example="Alternative Introduction To Computing A (NOT REQUIRED IN THE REQUEST)"),
        "information": fields.String(required=False, example="Alternative description (NOT REQUIRED IN THE REQUEST)"),
    }
)

courseDescDetails = api.model("For changing a course's description",
    {
        "id": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852"),
        "description": fields.String(required=True, example="New markdown for the course's homepage (NOT REQUIRED IN THE REQUEST)")
    }
)

courseReportDetails = api.model("For reporting a particular course",
    {
        "courseID": fields.String(required=True, example="5322c71754014f469ffc7f536978630d"),
        "reason": fields.String(required=True, example="Course has been deprecated, please remove")
    }
)

courseChangelogDetails = api.model("For getting a course's changelog",
    {
        "id": fields.String(required=True, example="6f14ce256d224b04a482ac29025d61ef")
    }
)

courseFollowDetails = api.model("For following a course",
    {
        "id": fields.String(required=True, example="6f14ce256d224b04a482ac29025d61ef")
    }
)

courseChangelogDetails = api.parser()
courseChangelogDetails.add_argument('id', required=True, help="CourseID of the course you want to get the changelogs for", location="args")
