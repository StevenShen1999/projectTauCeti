import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 addCourseListToDB.py [localPostgresPassword]")
    exit()
os.environ['SQLPassword'] = sys.argv[1]


from app import db
from models.courses import Courses
from models.unis import University
from uuid import uuid4

unswID = None

def initialiseCourses():
    allCourses = Courses.query.filter_by().all()
    if allCourses:
        if len(allCourses) > 500:
            print("Already Initialised The CourseList.JSON file")
            return

    with open("courseList.json", "r") as file:
        courseString = file.readlines()

    for i in courseString:
        for char in ["\"", "[", "]", ","]:
            i = i.replace(char, "")
        stringToList = i.split(' - ')
        courseCode, courseName = stringToList[0], stringToList[1]
        course = Courses(id=str(uuid4().hex), code=courseCode, name=courseName[:-1],
            university=unswID)
        db.session.add(course)

    db.session.commit()

    print('''
    ||||||||||||||||||||||||||||||||||||||
    ||||||||| All courses added ||||||||||
    ||||||||||||||||||||||||||||||||||||||
    ''')
    return True

def initialiseUnis():
    allUnis = University.query.filter_by().all()
    if allUnis:
        if len(allUnis) > 30:
            print("Already Initialised The UniList.txt file")
            return

    with open("UniList.txt", "r") as file:
        allUnis = file.readlines()

    for uni in allUnis:
        uni = uni.rstrip()
        university = University(id=str(uuid4().hex), name=uni)
        if (uni == "University of New South Wales"):
            global unswID
            unswID = university.id
        db.session.add(university)

    db.session.commit()

    print('''
    ||||||||||||||||||||||||||||||||||||||
    ||||||| All Universities added |||||||
    ||||||||||||||||||||||||||||||||||||||
    ''')

    return True


if __name__ == "__main__":
    status0 = initialiseUnis()
    status1 = initialiseCourses()

    if (not status0):
        print("Adding Unis Not Successful, Please Check Above Log")
    if (not status1):
        print("Adding Courses Not Successful, Please Check Above Log")