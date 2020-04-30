from namespaces.users import api
from flask_restplus import fields

userReportDetails = api.model("For reporting a particular user",
    {
        "userID": fields.String(required=True, example="wRXGpNIjhgLIvzWs"),
        "reason": fields.String(required=True, example="I dislike this guy's face.")
    }
)