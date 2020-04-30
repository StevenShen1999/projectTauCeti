from app import db
from flask_sqlalchemy import SQLAlchemy

class Courses(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Text, primary_key=True)
    code = db.Column(db.String(8), nullable=False)
    name = db.Column(db.Text, nullable=False)
    #semester = db.Column(db.String(4), nullable=False)
    information = db.Column(db.Text, nullable=True)
    university = db.Column(db.Text, nullable=False)

    _notes = db.relationship("Notes", uselist=False, back_populates="_course")
    createdby = db.Column(db.Text, db.ForeignKey('users.id'), nullable=True)
    _created = db.relationship("Users", back_populates="_courses")

    _messages = db.relationship("Messages", uselist=False, back_populates="_course")
    # NOTE: Potentially we can have Country/State here as well