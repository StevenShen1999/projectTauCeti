from app import db
from uuid import uuid4
from datetime import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
    email = db.Column(db.Text, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)
    activated = db.Column(db.Boolean, default=True, nullable=False)
    points = db.Column(db.Integer, default=0, nullable=False)
    link = db.Column(db.Text, nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False)
