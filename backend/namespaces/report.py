from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with

api = Namespace("report", description="APIs to handle \
    reports, reporting users, comments, notes")

from app import db

# All functions here are stubs, placeholders APIs to handle reporting in the future
# THe process goes like this:
# The user clicks on the report button next to the user, note, course
# All admins (or selected admins responsible for handling complaints) receive it in their inbox
# Admins could then take action to delete/edit comments, posts

@api.route("/user")
class ReportUser(Resource):
    def post(self):
        return "Success"

@api.route("/note")
class ReportNote(Resource):
    def post(self):
        return "Success"

@api.route("/course")
class ReportCourse(Resource):
    def post(self):
        return "Success"