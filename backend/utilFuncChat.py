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
    id = curs.fetchone[0]

    return id

def removeChat(messageID):
    msgStatus = checkMessage(messageID)
    if (msgStatus == False):
        return "Message doesn't exist"
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("delete from messages where messageid=?", (messageID,))
    conn.commit()

def checkMessage(messageID):
    conn = utilFunc.create_connection()
    curs = conn.cursor()
    curs.execute("select * from messages where messageid=?", (messageID,))
    conn.commit()
    result = curs.fetchone()
    return False if result != None else True