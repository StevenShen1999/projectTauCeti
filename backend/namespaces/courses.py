from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with, validate_with_args

api = Namespace("courses", description="APIs to handle courses related queries")

from models.courses import Courses
from models.notes import Notes
from app import db
from models.coursesModels import *
from schemas.courseSchemas import *
from models.notesModels import courseNotesDetails
from schemas.noteSchemas import courseNoteSchema
from util.authServices import validateToken
from flask import jsonify
from util.emailServices import sendRequestEmail

@api.route("/")
class EventRegister(Resource):
    @api.response(200, "{'message': 'Success', 'courseID': '5322c71754014f469ffc7f536978630d'}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(409, "Course with this course code at this semester already exists")
    @api.expect(courseCreationDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to create a course, requires a JWT Token of a valid user")
    @validate_with(CourseRegistrationSchema)
    @validateToken()
    def post(self, token_data, data):
        exists = Courses.query.filter_by(code=data.code, university=data.university).first()
        if exists: abort(409, "Course with this course code at this semester already exists")

        db.session.add(data)
        db.session.commit()

        return jsonify({"message": "Success", "courseID": data.id})

    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(courseDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to delete a course that already exists")
    @validate_with(CourseSchema)
    @validateToken(roleRequired=1)
    def delete(self, token_data, data):
        exists = Courses.query.filter_by(id=data['id']).first()
        if not exists: abort(409, "Course with this courseID doesn't exist")

        db.session.delete(exists)
        db.session.commit()

        return jsonify({"message": "Success"})

    @api.response(200, '''{'message': 'Success',\
         'payload': {'id': '', 'code': '', 'name': '', 'information': '', \
             'university': '', 'createdBy': '', 'notes': [{'id': 'skdfh', 'name': \
                 'A note that i uploaded', 'points': 123, 'price': 123, 'uploadTime': \
                     '2020-03-01 12:12:31', 'path': '/assets/images/', 'courseID': 'asdfkh', \
                     'uploaderID': 'askdjfh'}, {...}]}''')
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(courseNotesDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to get all notes attached to a specific courseID")
    @validate_with_args(courseNoteSchema)
    @validateToken()
    def get(self, token_data, data):
        course = Courses.query.filter_by(id=data['courseID']).first()
        if not course:
            abort(403, "Invalid Parametres (Invalid courseID)")
        payload = course.jsonifyObject()
        payload['notes'] = []

        exists = Notes.query.filter_by(courseid=data['courseID']).all()
        for i in exists:
            payload['notes'].append(i.jsonifyObject())
        return jsonify({"message": "Success", "payload": payload})


@api.route("/update")
class UpdateCourse(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(coursePatchDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="User this API (requires an admin account) to issue an update to the courses")
    @validate_with(CoursePatchSchema)
    @validateToken(roleRequired=1)
    def patch(self, token_data, data):
        course = Courses.query.filter_by(id=data['id']).first()
        if not course: abort(403, "Invalid courseID (doesn't exist)")

        if 'name' in data:
            course.name = data['name']
        if 'information' in data:
            course.information = data['information']

        db.session.add(course)
        db.session.commit()
        return jsonify({"message": "Success"})

    # To update information about a course, we send this package to admin accounts 
    # and process request from an alternative route
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(500, "Mail services not working, check settings and log and try again later.")
    @api.expect(coursePatchDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to request an update to a course's information (only for admins)\
        Note this API accepts a new name and/or information to update the course (with the courseID)\
        with, only one is required, don't include the other one in the request if they are not being updated")
    @validate_with(CoursePatchSchema)
    @validateToken()
    def post(self, token_data, data):
        course = Courses.query.filter_by(id=data['id']).first()
        if not course: abort(403, "Invalid courseID (doesn't exist)")

        payload = [] # Convert the payload here to comply with the requestEmail format
        if 'name' in data:
            payload.append(f"oldName: {course.name}\nnewName: {data['name']}\n")
        if 'information' in data:
            payload.append(f"oldDescription: {course.information}\nnewDescription: {data['information']}\n")
        if not payload:
            return jsonify({"message": 'Success', "payload": "Nothing Requested"})
        payload = ''.join(payload)

        emailStatus = sendRequestEmail('course', course.id, payload, token_data['email'], course.name)
        if emailStatus != "success": abort(500, "Mail services not working, check settings and log and try again later.")

        return jsonify({"message": "Success", "payload": "Request filed, please check back in 24 hours"})
