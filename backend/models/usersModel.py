from namespaces.users import api
from flask_restplus import fields
from werkzeug import FileStorage

userReportDetails = api.model("For reporting a particular user",
    {
        "userID": fields.String(required=True, example="wRXGpNIjhgLIvzWs"),
        "reason": fields.String(required=True, example="I dislike this guy's face.")
    }
)

userUpdateImageDetails = api.parser()
userUpdateImageDetails.add_argument("image", required=True, type=FileStorage, help="Put the new profile image here", location="files")

userUpdateDetails = api.model("For updating a particular user's information",
    {
        "username": fields.String(required=False, example="newUsername123123"),
        "email": fields.String(required=False, example="newEmail@memesmail.com")
    }
)