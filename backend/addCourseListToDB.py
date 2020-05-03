import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 addCourseListToDB.py [localPostgresPassword]")
    exit()
os.environ['SQLPassword'] = sys.argv[1]


from app import db
from models.courses import Courses
from uuid import uuid4

allCourses = Courses.query.filter_by().all()
if allCourses:
    print(allCourses[0].name)
    if len(allCourses) > 500:
        print("Already Initialised The CourseList.JSON file")
        exit(0)

with open("courseList.json", "r") as file:
    courseString = file.readlines()

for i in courseString:
    for char in ["\"", "[", "]", ","]:
        i = i.replace(char, "")
    stringToList = i.split(' - ')
    courseCode, courseName = stringToList[0], stringToList[1]
    course = Courses(id=str(uuid4().hex), code=courseCode, name=courseName[:-1],
        university="University of New South Wales")
    db.session.add(course)

db.session.commit()

print('''
||||||||||||||||||||||||||||||||||||||
||||||||| All courses added ||||||||||
||||||||||||||||||||||||||||||||||||||
''')
