import sqlite3
from sqlite3 import Error

def create_connection(databaseName):
    conn = None
    try:
        sqlite3.connect(r'../database/' + databaseName + r'.db')
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

def main():
    create_connection("userTable")

if __name__ == '__main__':
    main()