from app import db

class University(db.Model):
    __tablename__ = 'universities'

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    users = db.relationship("Users", uselist=True, back_populates="_uni")
    courses = db.relationship("Courses", uselist=True, back_populates="_uni")

    def jsonifySelf(self):
        return {
            'id': self.id,
            'name': self.name,
            'courses': self.getCourses()
            'users': self.getUsers()
        }

    def getCourse(self, courseCode):
        for course in self.courses:
            if course.code == courseCode:
                return course

        return None

    def getUsers(self):
        return [user.getUserInfoSimplified for user in self.users]

    def getCourses(self):
        return [course.jsonifyObject for course in self.courses]