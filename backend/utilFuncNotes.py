import sqlite3
from sqlite3 import Error
import utilFunc as util
import datetime

def saveFile(fileIn, course, name, userID):
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("insert into notes (course, name, filePath, dateLogged, nvotes, rating) values (?, ?, ?, ?, ?, ?)", (course, name, fileIn, datetime.datetime.now(), 0, 0,))
    conn.commit()
    curs.execute("select last_insert_rowid()")
    id = curs.fetchone()

    curs.execute("insert into submittion (uploader, notesID) values (?, ?)", (userID, id[0],))
    conn.commit()
    return (id[0])

def getFileName(fileID):
    filePath = checkFileExist(int(fileID))
    if (filePath == None):
        return "failed, no such file exists"
    return filePath[3]

def upvote(fileID):
    if (checkFileExist(fileID) == None):
        return "failed, no such file exists"
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select nvotes from notes where notesid=?", (int(fileID),))
    conn.commit()
    currentUpvotes = curs.fetchone()[0]
    curs.execute("update notes set nvotes=? where notesid=?", (currentUpvotes + 1, int(fileID),))
    conn.commit()
    return "success"

def getVotes(fileID):
    if (checkFileExist(int(fileID)) == None):
        return "failed, no such file exists"
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select nvotes from notes where notesid=?", (int(fileID), ))
    conn.commit()
    return curs.fetchone()[0]

def checkFileExist(fileID):
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select * from notes where notesid=?", (fileID,))
    conn.commit()
    return curs.fetchone()

def main():
    # saveFile(r"/mnt/c/Users/Steve\ Shen/COMP/project/tauCeti/database/test0.txt", "COMP9444", "Cool notes brah", "z5161616")
    # print(getFileName(3))
    checkFileExist(3)
    upvote(3)
    print(getVotes(3))

if __name__ == '__main__':
    main()