from app import db
from flask_sqlalchemy import SQLAlchemy

class Notes(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    uploadtime = db.Column(db.DateTime(timezone=True), nullable=False)
    path = db.Column(db.Text, nullable=False)

    courseid = db.Column(db.Text, db.ForeignKey('courses.id'), nullable=False)
    _course = db.relationship("Courses", back_populates="_notes")
    uploaderid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    _uploader = db.relationship("Users", back_populates="_notes")

    _messages = db.relationship("Messages", uselist=False, back_populates="_note")

    def jsonifyObject(self):
        payload = {}
        payload['id'] = self.id
        payload['name'] = self.name
        payload['points'] = self.points
        payload['price'] = self.price
        payload['uploadtime'] = self.uploadtime
        payload['path'] = self.path
        payload['courseid'] = self.courseid
        payload['uploaderid'] = self.uploaderid

        return payload

    def vote(self, value):
        self.points += value