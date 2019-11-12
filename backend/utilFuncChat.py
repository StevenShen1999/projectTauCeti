from sqlite3 import Error
import sqlite3
import utilFunc
import datetime

def insertChat(message, course, sender):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("insert into messages (course, sender, timesent, message) values (?, ?, ?, ?)", (course, sender, datetime.datetime.now(), message,))
    conn.commit()
    curs.execute("select last_insert_rowid()")
    messageID = curs.fetchone()[0]

    return messageID

def removeChat(messageID):
    msgStatus = checkMessage(messageID)
    if (msgStatus == False):
        return "Message doesn't exist"
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("delete from messages where messageid=?", (messageID,))
    conn.commit()
    return "success"

def getChat (course):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("select * from messages where course=?", (course,))
    conn.commit()
    return curs.fetchall()

def checkMessage(messageID):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("select * from messages where messageid=?", (messageID,))
    conn.commit()
    result = curs.fetchone()
    return False if result != None else True

def main():
    insertChat("lel, Yang lmao", "COMP9444", "z5161616")
    insertChat("WHATEVER la", "COMP9444", "z5161616")
    print(getChat("COMP9444"))

if __name__ == '__main__':
    main()