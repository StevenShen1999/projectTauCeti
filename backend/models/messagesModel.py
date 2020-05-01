from namespaces.messages import api
from flask_restplus import fields
from datetime import datetime

messageCreationDetails = api.model("For creating a message (for instant messaging)",
    {
        "content": fields.String(required=True, example="Yo wassup my g's"),
        "courseID": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852")
    }
)

'''
messagePollingDetails = api.model("For all the messages send since the last increment of the course group chat",
    {
        "previousIncrement": fields.DateTime(dt_format='iso8601',
            required=True, example="2020-04-09T11:13:33Z", description="Needs to be a UTC timecode"),
        "courseID": fields.String(required=True, example="54e80ff91ae94f62ac3033c01b41b852")
    }
)
'''

messagePollingDetails = api.parser()
messagePollingDetails.add_argument("previousIncrement", required=True,
    type=datetime, help="2020-04-09T11:00:00Z", location="args")
messagePollingDetails.add_argument("courseID", required=True,
    type=str, help="5322c71754014f469ffc7f536978630d", location="args")
