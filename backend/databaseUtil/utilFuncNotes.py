import sqlite3
from sqlite3 import Error
from databaseUtil import utilFunc as util
import datetime
from databaseUtil import utilFuncCourses

def saveFile(fileIn, course, name, userID):
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("insert into notes (uploader, course, name, filePath, dateLogged, nvotes, rating) values (?, ?, ?, ?, ?, ?, ?)", (userID, course, name, fileIn, datetime.datetime.now(), 0, 0,))
    conn.commit()
    curs.execute("select last_insert_rowid()")
    fileID = curs.fetchone()

    conn.commit()
    conn.close()
    return (fileID[0])

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
    conn.close()
    return "success"

def getVotes(fileID):
    if (checkFileExist(int(fileID)) == None):
        return "failed, no such file exists"
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select nvotes from notes where notesid=?", (int(fileID), ))
    conn.commit()
    nvotes = curs.fetchone()[0]
    conn.close()
    return nvotes

def getCourseLadder(courseID):
    if (utilFuncCourses.checkCourse(courseID) == False):
        return "failed, no such course exists"
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select * from notes where course=? order by nvotes desc", (courseID,))
    conn.commit()
    notesRank = curs.fetchall()
    result = []
    for i, note in enumerate(notesRank):
        result.append({'rank': i + 1, 'notesID': note[0], 'notesName': note[3], 'nVotes': note[6], 'notesPublisher': note[1], 'notesPublishDate': note[5]})
    conn.close()
    return result

def getOverallLadder():
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select * from notes order by nvotes desc")
    conn.commit()
    notesRank = curs.fetchall()
    result = []
    for i, note in enumerate(notesRank):
        result.append({'rank': i + 1, 'notesID': note[0], 'notesName': note[3], 'course': note[2], 'nVotes': note[6], 'notesPublisher': note[1], 'notesPublishDate': note[5]})
    conn.close()
    return result

def checkFileExist(fileID):
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select * from notes where notesid=?", (fileID,))
    conn.commit()
    result = curs.fetchone()
    conn.close()
    return result

def getCourseNotes(courseID):
    conn = util.create_connection()
    curs = conn.cursor()
    curs.execute("select * from notes where course = ?", (courseID,))
    conn.commit()
    result = curs.fetchall()
    results = []
    for i in result:
        results.append({'notesID': i[0], 'uploader': i[1], 'course': i[2], 'name': i[3], 'filePath': i[4], 'dateLogged': i[5], 'nVotes': i[6]})
    return results

def main():
    '''
    for i in range(0, 3):
        saveFile(r"../database/test0.txt", "COMP9444", "Cool notes brah", "z5161616")
    '''
    # print(getFileName(3))
    checkFileExist(3)
    for i in range(0, 6):
        upvote(3)
    print(getVotes(3))
    print(getCourseLadder('COMP9444'))

if __name__ == '__main__':
    main()