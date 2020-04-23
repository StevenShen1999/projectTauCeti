from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app, version="0.0.1", title='TauCeti',
description="TauCeti Notes Sharing App's Backend Server, pre-Alpha")

from namespaces.courses import api as courses
from namespaces.notes import api as notes
from namespaces.uploads import api as uploads # Might deprecate this
from namespaces.users import api as users
from namespaces.auth import api as auth

api.add_namespace(courses)
api.add_namespace(notes)
api.add_namespace(uploads)
api.add_namespace(users)
api.add_namespace(auth)

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)