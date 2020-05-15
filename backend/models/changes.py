from app import db

class Changes(db.Model):
    __tablename__ = 'changes'

    id = db.Column(db.Text, primary_key=True)
    time = db.Column(db.DateTime(timezone=True), nullable=False)

    namediff = db.Column(db.Text, nullable=True)
    informationdiff = db.Column(db.Text, nullable=True)
    descriptiondiff = db.Column(db.Text, nullable=True)

    changerid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    _changer = db.relationship("Users", back_populates="_changes")
    courseid = db.Column(db.Text, db.ForeignKey('courses.id'), nullable=False)
    _course = db.relationship("Courses", back_populates="_changes")

    def jsonifyObject(self):
        payload = {}
        payload['id'] = self.id
        payload['time'] = self.time
        if self.namediff:
            payload['nameDiff'] = self.namediff
        if self.informationdiff:
            payload['informationDiff'] = self.informationdiff
        if self.descriptiondiff:
            payload['descriptionDiff'] = self.descriptiondiff

        payload['changerID'] = self.changerid
        payload['courseID'] = self.courseid

        return payload