import sqlite3
import re
from sqlite3 import Error
import utilFunc as util

def main():
    createNotesSQL = '''
        CREATE TABLE IF NOT EXISTS notes (
            notesID integer primary key autoincrement,
            uploader text not null references users(studentID),
            course text not null references course(coursecode),
            name text not null,
            filePath text not null,
            dateLogged date not null,
            nvotes integer not null,
            rating double not null
        );
    '''
    conn = util.create_connection()
    util.createTable(conn, createNotesSQL)

    # FIXME: Potentially, we can add a last sign-in field here to faciliate future JWT session token implementations
    createUsersSQL = '''
        CREATE TABLE IF NOT EXISTS users (
            studentID text not null,
            password text not null,
            token text,
            primary key (studentID)
        );
    '''
    util.createTable(conn, createUsersSQL)

    """ DEPRECATED, MOVED THE UPLOADER COLUMN INTO THE NOTES TABLE
    createSubmittedSQL = '''
        CREATE TABLE IF NOT EXISTS submittion (
            uploader text not null references users(studentID),
            notesID integer not null references notes(notesID),
            primary key (uploader, notesID)
        );
    '''
    util.createTable(conn, createSubmittedSQL)
    """

    createChatSQL = '''
        CREATE TABLE IF NOT EXISTS messages (
            messageID integer primary key autoincrement,
            course text not null references course(courseCode),
            sender text not null references users(studentID),
            timeSent datetime not null,
            message text not null
        )
    '''
    util.createTable(conn, createChatSQL)

    createCourseSQL = '''
        CREATE TABLE IF NOT EXISTS course (
            courseCode text not null primary key,
            courseName text not null,
            description text
        );
    '''
    util.createTable(conn, createCourseSQL)

    courseList = open('./courseList.json', 'rb')
    courseListLines = courseList.readlines()
    for line in courseListLines:
        #print(line)
        courseCodes = re.search('[A-Z]{4}[0-9]{4}', str(line))
        courseNames = re.search(' ([A-Za-z &]+)', str(line))

        conn = util.create_connection()
        curs = conn.cursor()
        curs.execute("insert into course (courseCode, courseName) values (?, ?)", (courseCodes.group(), courseNames[1]))
        conn.commit()
    

if __name__ == '__main__':
    main()