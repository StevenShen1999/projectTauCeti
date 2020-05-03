from flask import Flask, send_from_directory
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
from namespaces.notes import api as notes
from namespaces.courses import api as courses
from namespaces.users import api as users
from namespaces.auth import api as auth
from namespaces.messages import api as messages
from namespaces.report import api as report

api.add_namespace(notes, path='/notes')
api.add_namespace(courses, path='/courses')
api.add_namespace(users, path='/users')
api.add_namespace(auth, path='/auth')
api.add_namespace(messages, path='/messages')
api.add_namespace(report, path='/report')

# File Upload
if (app.config['ENV'] == 'development'):
    @app.route('/assets/images/<path:path>')
    def send_images(path):
            return send_from_directory('../assets/images/', path)

    if not os.path.exists("../assets/images/"):
        os.makedirs("../assets/images")

if (app.config['ENV'] == 'development'):
    app.config['UPLOAD_FOLDER'] = f"{os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))}/assets/images/"
elif (app.config['ENV'] in ['production','test']):
    app.config['UPLOAD_FOLDER'] = f"/var/www/static/assets/images/"

# CORS
CORS(app)

## Dur to a SQLAlchemy quirk, use run.py to run the server