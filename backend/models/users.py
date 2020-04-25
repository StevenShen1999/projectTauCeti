from app import db
from uuid import uuid4
from flask_sqlalchemy import SQLAlchemy

class Users(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.Text, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)
    activated = db.Column(db.Boolean, default=True, nullable=False)
    points = db.Column(db.Integer, default=0, nullable=False)
    link = db.Column(db.Text, nullable=False)
    createddate = db.Column(db.DateTime, nullable=False)

    _notes = db.relationship("Notes", uselist=False, back_populates="_uploader")
    _courses = db.relationship("Courses", uselist=False, back_populates="_created")