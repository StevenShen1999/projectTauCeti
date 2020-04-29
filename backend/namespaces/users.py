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

@api.route("/<string:userID>")
class UserBaseAPI(Resource):
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to update user's information. (NOT YET IMPLEMENTED).")
    def post(self, token_data, data):
        return "Success"

    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}}, 
        description="Use this API to get a user's information. (NOT YET IMPLEMENTED).")
    def get(self, token_data, data):
        return "Success"
