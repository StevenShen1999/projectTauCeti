from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with

api = Namespace("courses", description="APIs to handle courses related queries")

from models.courses import Courses
from app import db
from models.coursesModels import *
from schemas.courseSchemas import *
from util.authServices import validateToken
from flask import jsonify

@api.route("/")
class EventRegister(Resource):
    @api.response(200, "{'status': 'Success', 'courseID': ''}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.response(409, "Course with this course code at this semester already exists")
    @api.expect(courseCreationDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to create a course, requires a JWT Token of a valid user")
    @validate_with(CourseRegistrationSchema)
    @validateToken()
    def post(self, token_data, data):
        exists = Courses.query.filter_by(code=data.code, semester=data.semester, university=data.university).first()
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
    @validateToken()
    def delete(self, token_data, data):
        exists = Courses.query.filter_by(id=data['id']).first()
        if not exists: abort(409, "Course with this courseID doesn't exist")

        db.session.delete(exists)
        db.session.commit()

        return jsonify({"message": "Success"})

    @api.doc(description="Stub API, not yet implemented")
    def get(self):
        return 0