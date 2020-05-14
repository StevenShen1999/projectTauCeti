from flask_restplus import Resource, abort, Namespace
from util.validationServices import validate_with, validate_with_args

# This is for instant messaging (for chatrooms)
api = Namespace("messages", description="APIs to handle messages related queries")

from models.messages import Messages
from models.courses import Courses
from models.users import Users
from app import db
from models.messagesModel import *
from schemas.messageSchemas import *
from util.authServices import validateToken
from flask import jsonify, abort
from sqlalchemy import asc

@api.route("/")
class CreateMessage(Resource):
    @api.response(200, "{'message': 'Success', 'messageID': ''}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(messageCreationDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to write messages to course specific chatrooms")
    @validate_with(MessageCreationSchema)
    @validateToken()
    def post(self, token_data, data):
        if not Courses.query.filter_by(id=data.courseid).first():
            abort(403, "Not a valid courseID")
        data.senderid = token_data['id']

        db.session.add(data)
        db.session.commit()
        return jsonify({"message": "Success", "messageID": data.id})

    # A get request should also be included, however, currently ensure what the behaviour
    # of the get api should be


@api.route("/course")
class GetCourseMessages(Resource):
    @api.response(200, "{'message': 'Success', 'messages': \
        ['timePosted': '2020-03-13', 'sender': 'n1j23hiADhk', 'content': 'Cocaine for sale'}")
    @api.response(400, "Missing Parametres")
    @api.response(403, "Invalid Parametres")
    @api.expect(messagePollingDetails)
    @api.doc(params={'Authorization': {'in': 'header', 'description': 'Put the JWT Token here'}},
        description="Use this API to get the messages in a particular course \
            (specify the increments of which you want the messages from) in chronological order")
    @validate_with_args(MessagePollingSchema)
    @validateToken()
    def get(self, token_data, data):
        if not Courses.query.filter_by(id=data['courseID']).first():
            abort(403, "Not a valid courseID")

        allMessages = Messages.query.join(Users, Users.id==Messages.senderid).\
            add_columns(Users.username).filter(Messages.courseid==data['courseID'], \
                Messages.time>=data['previousIncrement']).order_by(asc(Messages.time)).all()

        #allMessagesJoined = allMessages.join(Users).filter(Users.id==Messages.senderid).all()
        #print(allMessagesJoined)
        payload = []
        for i in allMessages:
            payload.append(i[0].jsonifyObject())
            payload[-1].pop('senderID')
            payload[-1]['username'] = i[1]

        return jsonify({"message": "Success", "messages": payload})