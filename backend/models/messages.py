from app import db
from flask_sqlalchemy import sqlalchemy

# Stub Class
class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Text, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime(timezone=True), nullable=False)

    noteid = db.Column(db.Text, db.ForeignKey('notes.id'), nullable=False)
    _note = db.relationship("Notes", back_populates="_messages")
    senderid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    _sender = db.relationship("Users", back_populates="_messages")

    def jsonifyObject(self):
        payload = {}

        return payload