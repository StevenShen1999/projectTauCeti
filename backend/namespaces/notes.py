from flask_restplus import abort, Resource, Namespace
from util.validationServices import validate_with, validate_with_form, validate_with_args

api = Namespace("notes", description="APIs to handle notes related queries")

from models.notes import Notes
from models.users import Users
from app import db
from models.notesModels import *
from schemas.noteSchemas import *
from util.authServices import validateToken
from flask import jsonify, request
from util.fileServices import uploadImages

@api.route("/")
class notesBaseAPI(Resource):
    @api.response(200, "{'message': 'Success', 'noteID': ''}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(notesCreationDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to create and upload a note.\
            Beware that the input parametres need to be passed in as request.form!!!!!!!")
    @validate_with_form(creationSchema)
    @validateToken()
    def post(self, token_data, data):
        # Since marshmallow can't validate files, need to validate that the files are in the request
        if not request.files:
            abort(400, "Missing Parametres")

        data.uploaderid = token_data['id']

        uploadStatus = uploadImages(request.files['file'])
        if not isinstance(uploadStatus, tuple): abort(403, uploadStatus)
        data.path = uploadStatus[0]

        db.session.add(data)
        db.session.commit()

        return jsonify({'message': 'Success', 'noteID': data.id})


    @api.response(200, '''{'message': 'Success',\
         'payload': {'id': 'skdfh', 'name': 'A note that i uploaded', \
             'points': 123, 'price': 123, 'uploadTime': '2020-03-01 12:12:31', \
                 'path': '/assets/images/', 'courseID': 'asdfkh', \
                     'uploaderID': 'askdjfh'}}''')
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    # Gets can't have bodies, need to validate another function to validate query string
    @api.expect(notesDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to get the infomation of a note")
    @validate_with_args(notesGeneralSchema)
    @validateToken()
    def get(self, token_data, data):
        exists = Notes.query.filter_by(id=data['noteID']).first()
        if not exists: abort(403, "Invalid Parametres (No such note)")

        payload = exists.jsonifyObject()
        return jsonify({'message': 'Success', 'payload': payload})


    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(401, "Access Denied, Not The Note Owner")
    @api.response(403, "Invalid Parametres")
    @api.expect(notesDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to delete a note")
    @validate_with_args(notesGeneralSchema)
    @validateToken()
    def delete(self, token_data, data):
        exists = Notes.query.filter_by(id=data['noteID']).first()
        if not exists: abort(403, "Invalid Parametres (No such note)")

        if exists.uploaderid != token_data['email']: abort(401, "Access Denied, Not The Note Owner")

        db.session.delete(exists)
        db.session.commit()

        return jsonify({'message': 'Success'})


@api.route("/vote")
class NoteVoter(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(notesVoterDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to vote for a note (either upvote or downvote)")
    @validate_with_args(noteVoterSchema)
    @validateToken()
    def post(self, token_data, data):
        note = Notes.query.filter_by(id=data['noteID']).first()
        user = Users.query.filter_by(email=token_data['email']).first()
        if not note: abort(403, "Invalid Parametres (No such note)")

        note.vote(data['vote'])
        user.vote(data['vote'])

        db.session.add(note)
        db.session.commit()

        return jsonify({"message": "Success"})

    # For admins to delete bogus votes
    def delete(self, token_data, data):
        return "Success"


@api.route("/course", endpoint='course')
class CourseNotes(Resource):
    @api.response(200, '''{'message': 'Success',\
         'payload': [{'id': 'skdfh', 'name': 'A note that i uploaded', \
             'points': 123, 'price': 123, 'uploadTime': '2020-03-01 12:12:31', \
                 'path': '/assets/images/', 'courseID': 'asdfkh', \
                     'uploaderID': 'askdjfh'}, {...}]}''')
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(courseNotesDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to get all notes attached to a specific courseID")
    @validate_with_args(courseNoteSchema)
    @validateToken()
    def get(self, token_data, data):
        exists = Notes.query.filter_by(courseid=data['courseID']).all()
        payload = []
        for i in exists:
            payload.append(i.jsonifyObject())
        return jsonify({"message": "Success", "payload": payload})