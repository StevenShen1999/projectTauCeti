from app import db
from uuid import uuid4

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Text, primary_key=True)
    email = db.Column(db.Text, nullable=False, index=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Text, nullable=False)
    activated = db.Column(db.Boolean, default=True, nullable=False)
    points = db.Column(db.Integer, default=0, nullable=False)
    link = db.Column(db.Text, nullable=False)
    createddate = db.Column(db.DateTime(timezone=True), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    lastloggedin = db.Column(db.DateTime(timezone=True), nullable=True)
    verificationcode = db.Column(db.Text, nullable=True)
    failedlogins = db.Column(db.Integer, nullable=False)
    lockeduntil = db.Column(db.DateTime(timezone=True), nullable=True)
    # Need a section here for the referred by person

    _notes = db.relationship("Notes", uselist=False, back_populates="_uploader")
    _courses = db.relationship("Courses", uselist=True, back_populates="_created")
    _messages = db.relationship("Messages", uselist=True, back_populates="_sender")

    def jsonifyObject(self):
        payload = {}
        payload['id'] = self.id
        payload['email'] = self.email
        payload['username'] = self.username
        payload['activated'] = self.activated
        payload['points'] = self.points
        payload['link'] = self.link
        payload['createddate'] = self.createddate
        payload['role'] = self.role
        payload['lastloggedin'] = self.lastloggedin

    def vote(self, value):
        self.points += value