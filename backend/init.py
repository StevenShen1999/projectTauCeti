import sqlite3
from sqlite3 import Error
import utilFunc as util

def main():
    createNotesSQL = '''
        CREATE TABLE IF NOT EXISTS notes (
            notesID integer primary key autoincrement,
            course text not null,
            name text not null,
            filePath text not null,
            dateLogged date not null,
            nvotes integer not null,
            rating double not null
        );
    '''
    conn = util.create_connection()
    util.createTable(conn, createNotesSQL)

    createUsersSQL = '''
        CREATE TABLE IF NOT EXISTS users (
            studentID text not null,
            password text not null,
            token text,
            primary key (studentID)
        );
    '''
    util.createTable(conn, createUsersSQL)

    createSubmittedSQL = '''
        CREATE TABLE IF NOT EXISTS submittion (
            uploader text not null references users(studentID),
            notesID integer not null references notes(notesID),
            primary key (uploader, notesID)
        );
    '''
    util.createTable(conn, createSubmittedSQL)

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


if __name__ == '__main__':
    main()