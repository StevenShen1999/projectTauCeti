from app import db
from flask_sqlalchemy import SQLAlchemy

class Courses(db.Model):
    id = db.Column(db.Text, primary_key=True)
    code = db.Column(db.String(8), nullable=False)
    name = db.Column(db.Text, nullable=False)
    semester = db.Column(db.String(4), nullable=False)
    university = db.Column(db.Text, nullable=False)
    # NOTE: Potentially we can have Country/State here as well