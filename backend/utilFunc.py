import sqlite3
import base64
from sqlite3 import Error
import jwt
import hashlib, binascii
import os
import datetime

key = "j34g1k2j5g1345hkj34g52bc4gh3f*!@^#&(())"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r'../database/everything.db')
    except Error as e:
        print(e)
    return conn

def createTable(conn, sql):
    try:
        curs = conn.cursor()
        curs.execute(sql)
    except Error as e:
        print(e)

def runQuery(conn, sql, arg):
    try:
        curs = conn.cursor()
        curs.execute(sql, arg)
    except Error as e:
        print(e)

def createUser(userID, password):
    if (checkUserExists(userID) == True):
        return "user already exists"
    password = hashPassword(password)
    conn = create_connection()
    curs = conn.cursor()
    curs.execute("insert into users(studentid, password, token) values (?, ?, ?)", (userID, password, None,))
    conn.commit()
    return "success"
    
def login(userID, password):
    conn = create_connection()
    curs = conn.cursor()
    curs.execute("select * from users where studentid = ?", (userID,))
    conn.commit()
    result = curs.fetchone()
    if (result == None):
        return "user does not exist"
    else:
        result = verifyPassword(password, result[1])
        if (result == False):
            return "Password incorrect"
        else:
            token = createToken(userID)
            print(token)
            print(jwt.decode(token, key, algorithms=['HS256']))
            curs.execute("update users set token=? where studentid=?", (token, userID,))
            conn.commit()
            return token

def logout(userID):
    userInfo = checkUserExists(userID)
    if (userInfo == False):
        return "User does not exist"

    conn = create_connection()
    curs = conn.cursor()
    curs.execute("update users set token=? where studentid=?", (None, userID,))
    conn.commit()
    return "success"

def hashPassword(password):
    return hashlib.sha512(password.encode()).hexdigest()

def verifyPassword(passwordGiven, passwordExists):
    pwdhash = hashlib.sha512(passwordGiven.encode()).hexdigest()
    return pwdhash == passwordExists

def createToken(userID):
    payload = {
        'iat': datetime.datetime.utcnow(),
        'sub': userID
    }

    return jwt.encode(payload, key, 'HS256').decode('utf-8')

def verifyToken(token):
    try:
        payload = jwt.decode(token, key)
        return payload['sub']
    except jwt.InvalidTokenError:
        return 'Invalid token. PLease log in again'

def checkUserExists(userID):
    conn = create_connection()
    curs = conn.cursor()
    curs.execute("select * from users where studentid = ?", (userID,))
    conn.commit()
    result = curs.fetchone()
    return False if result == None else True


def main():
    create_connection()
    # print(checkUserExists("z5161616"))
    createUser("z5161616", "990928ss")
    # print(checkUserExists("z5161616"))
    login("z5161616", "990928ss")

if __name__ == '__main__':
    main()