from app import db

class Follows(db.Model):
    __tablename__ = 'follows'

    userid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False, primary_key=True)
    _follower = db.relationship("Users", back_populates="_follows")
    courseid = db.Column(db.Text, db.ForeignKey('courses.id'), nullable=False, primary_key=True)
    _course = db.relationship("Courses", back_populates="_follows")
