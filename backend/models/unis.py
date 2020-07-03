from app import db

class University(db.Model):
    __tablename__ = 'universities'

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    users = db.relationship("Users", uselist=True, back_populates="_uni")
    courses = db.relationship("Courses", uselist=True, back_populates="_uni")