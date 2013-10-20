import sqlite3
import sys

def reset():
    connect = sqlite3.connect('userdata.db')
    cur=connect.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("CREATE TABLE Users(Username TEXT, Password TEXT)")

def authenticate(username, password):
    connect = sqlite3.connect('userdata.db')
    cur = connect.cursor()
    with connect:
        cur.execute("SELECT Password from Users WHERE Username = '%s'" %username)
        row = cur.fetchall()
        if row == []: #username is not found
            return 1
        elif row[0][0] == password: #correct login info
            return 3
        else: #wrong password
            return 2

def register(username, password):
#sanitize inputs here
    
    connect = sqlite3.connect('userdata.db')
    cur=connect.cursor()
    if len(username) < 4:
        return 0
    if len(password) < 6:
        return 1
    with connect:
        cur.execute("SELECT * from Users WHERE Username = '%s'" %username)
        row = cur.fetchall()
        print row
        if row != []:
            return 2
        else: 
            cur.execute("INSERT INTO Users VALUES ('"+username +"','"+password+"');")
            connect.commit()

if __name__ == "__main__":
    register("jyin", "password")
    register("kevin", "password")
    register("steve", "awkwardcat")
    authenticate("jyin", "password")
