from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with

# This is for instant messaging (for chatrooms)
api = Namespace("messages", description="APIs to handle messages related queries")

from models.messages import Messages
from app import db
from flask import jsonify, abort

@api.route("/")
class CreateMessage(Resource):
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to write messages to course specific chatrooms")
    def post(self):
        return "Success"