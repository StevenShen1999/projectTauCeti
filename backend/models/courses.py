from app import db

class Courses(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Text, primary_key=True)
    code = db.Column(db.String(8), nullable=False)
    name = db.Column(db.Text, nullable=False)
    # NOTE: Information works as an overview of the course
    information = db.Column(db.Text, nullable=True)
    # NOTE: Description works as the user-editable markdown section
    description = db.Column(db.Text, nullable=True)

    _notes = db.relationship("Notes", uselist=True, back_populates="_course")
    createdby = db.Column(db.Text, db.ForeignKey('users.id'), nullable=True)
    _created = db.relationship("Users", back_populates="_courses")

    _messages = db.relationship("Messages", uselist=True, back_populates="_course")
    _changes = db.relationship("Changes", back_populates="_course")
    _follows = db.relationship("Follows", back_populates="_course")

    university = db.Column(db.Text, db.ForeignKey('universities.id'), nullable=False)
    _uni = db.relationship("University", back_populates="courses")
    # NOTE: Potentially we can have Country/State here as well

    def jsonifyObject(self):
        payload = {}
        payload['id'] = self.id
        payload['code'] = self.code
        payload['name'] = self.name
        payload['information'] = self.information
        payload['university'] = self.university
        payload['createdBy'] = self.createdby

        return payload