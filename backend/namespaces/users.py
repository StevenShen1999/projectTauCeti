from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with_args, validate_with, validate_with_form

api = Namespace('users', description="APIs to handle user related queries")

from models.users import Users
from app import db
from models.usersModel import *
from schemas.userSchemas import *
from util.authServices import validateToken
from flask import jsonify, request
from util.fileServices import uploadImages
from util.emailServices import sendReportEmail

@api.route("/")
class UserBaseAPI(Resource):
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to get a user's information. (NOT YET IMPLEMENTED).")
    @api.response(200, "Success")
    @api.response(400, "Invalid Parameters")
    @validateToken()
    def get(self, token_data):
        user = Users.query.filter_by(id=token_data['id']).first()

        if not user:
            abort(400, "Invalid Parameters (Not a valid token/id)")

        return jsonify(user.getUserInfo())

# Update tokenbearer's profile image
@api.route("/update/profileImage")
class UpdateUserImage(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(userUpdateImageDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to update the token bearer's profile image")
    @validateToken()
    def patch(self, token_data):
        if not request.files:
            abort(400, "Missing Parametres (New profile image not included in the request)")

        user = Users.query.filter_by(id=token_data['id']).first()

        imageStatus = uploadImages(request.files['image'])
        if not isinstance(imageStatus, tuple): abort(403, imageStatus)

        user.profileimage = imageStatus[0]
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Success"})

# Update tokenbearer's profile image
@api.route("/update/general")
class UpdateUserAccount(Resource):
    @api.response(200, "Success")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(userUpdateDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to update the token bearer's email or username")
    @validate_with(userUpdateDetails)
    @validateToken()
    def post(self, token_data, data):
        user = Users.query.filter_by(id=token_data['id']).first()

        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']

        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Success"})