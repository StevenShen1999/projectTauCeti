from databaseUtil import utilFunc

def insertDescription(description, course):
    courseExists = checkCourse(course)
    if (courseExists == False):
        return "Course doesn't exist"
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("update course set description = ? where courseCode = ?", (description, course,))
    conn.commit()
    conn.close()
    return "success"


def checkCourse(course):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("select * from course where courseCode = ?", (course,))
    conn.commit()
    result = curs.fetchone()
    conn.close()
    return None if result == None else result

def getCourse(course):
    result = checkCourse(course)
    if (result == None):
        return "Course does not exist"
    return result