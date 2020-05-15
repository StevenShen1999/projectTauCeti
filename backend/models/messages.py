from app import db

# For chatroom messages
class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Text, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime(timezone=True), nullable=False)

    courseid = db.Column(db.Text, db.ForeignKey('courses.id'), nullable=False)
    _course = db.relationship("Courses", back_populates="_messages")
    senderid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    _sender = db.relationship("Users", back_populates="_messages")

    def jsonifyObject(self):
        payload = {}
        payload['messageID'] = self.id
        payload['content'] = self.content
        payload['time'] = self.time
        payload['courseID'] = self.courseid
        payload['senderID'] = self.senderid

        return payload