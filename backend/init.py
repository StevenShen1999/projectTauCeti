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
            rating double not null,
        )
    '''
    conn = util.create_connection()
    util.createTable(conn, createNotesSQL)

    createUsersSQL = '''
        CREATE TABLE IF NOT EXISTS users (
            studentID text not null,
            password text not null,
            token text,
            primary key (studentID)
        )
    '''
    util.createTable(conn, createUsersSQL)

    createSubmittedSQL = '''
        CREATE TABLE IF NOT EXISTS submittion (
            uploader text not null references users(studentID),
            notes integer not null references notes(notesID),
            primary key (uploader, notes)
        )
    '''
    util.createTable(conn, createSubmittedSQL)


if __name__ == '__main__':
    main()