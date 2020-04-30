from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with

api = Namespace("report", description="APIs to handle \
    reports, reporting users, comments, notes")

from flask import jsonify

from app import db
from util.emailServices import sendReportEmail
from util.authServices import validateToken

from models.users import Users
from models.usersModel import userReportDetails
from schemas.userSchemas import ReportUserSchema

from models.courses import Courses
from models.coursesModels import courseReportDetails
from schemas.courseSchemas import CourseReportSchema

from models.notes import Notes
from models.notesModels import notesReportDetails
from schemas.noteSchemas import noteReportSchema

# All functions here are stubs, placeholders APIs to handle reporting in the future
# THe process goes like this:
# The user clicks on the report button next to the user, note, course
# All admins (or selected admins responsible for handling complaints) receive it in their inbox
# Admins could then take action to delete/edit comments, posts

@api.route("/user")
class ReportUser(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(500, "Mail services not working, check settings and log and try again later.")
    @api.expect(userReportDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to report a user")
    @validate_with(ReportUserSchema)
    @validateToken()
    def post(self, token_data, data):
        user = Users.query.filter_by(id=data['userID']).first()
        if not user: abort(403, "Not a valid userID, try reporting someone else :)")

        emailStatus = sendReportEmail("user", data['userID'], data['reason'],
            token_data['email'], user.email)

        if emailStatus != "success":
            abort(500, "Mail services not working, check settings and log and try again later.")
        return jsonify({"message": "Success", "payload": "Report filed, upon completion of an examination,\
            the results will be notified to you by email"})

@api.route("/note")
class ReportNote(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(500, "Mail services not working, check settings and log and try again later.")
    @api.expect(notesReportDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to report a user")
    @validate_with(noteReportSchema)
    @validateToken()
    def post(self, token_data, data):
        note = Notes.query.filter_by(id=data['noteID']).first()
        if not note: abort(403, "Not a valid noteID, try reporting someone else :)")

        emailStatus = sendReportEmail("note", data['noteID'], data['reason'],
            token_data['email'], note.name)

        if emailStatus != "success":
            abort(500, "Mail services not working, check settings and log and try again later.")
        return jsonify({"message": "Success", "payload": "Report filed, upon completion of an examination,\
            the results will be notified to you by email"})

@api.route("/course")
class ReportCourse(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(500, "Mail services not working, check settings and log and try again later.")
    @api.expect(courseReportDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to report a user")
    @validate_with(CourseReportSchema)
    @validateToken()
    def post(self, token_data, data):
        course = Courses.query.filter_by(id=data['courseID']).first()
        if not course: abort(403, "Not a valid userID, try reporting someone else :)")

        emailStatus = sendReportEmail("course", data['courseID'], data['reason'],
            token_data['email'], course.name)

        if emailStatus != "success":
            abort(500, "Mail services not working, check settings and log and try again later.")
        return jsonify({"message": "Success"})