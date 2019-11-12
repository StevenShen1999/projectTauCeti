import utilFunc

def insertDescription(description, course):
    courseExists = checkCourse(course)
    if (courseExists == False):
        return "Course doesn't exist"
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("update course set description = ? where courseCode = ?", (description, course,))
    conn.commit()
    return "success"


def checkCourse(course):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("select * from course where courseCode = ?", (course,))
    conn.commit()
    result = curs.fetchone()
    return False if result == None else True