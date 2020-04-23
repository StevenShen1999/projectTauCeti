from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from config import Configuration

# Flask 
app = Flask(__name__)
api = Api(app, version="0.0.1", title='TauCeti',
description="TauCeti Notes Sharing App's Backend Server, pre-Alpha")

# Configuring
app.config.from_object(Configuration)

# SQLALchemy
db = SQLAlchemy(app)

# Flask-restplus
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

# CORS
CORS(app)

## Dur to a SQLAlchemy quirk, use run.py to run the server