import sqlite3 as sql
import sys

connect = None
cur = None
try:
    connect = sql.connect('userdata.db')
    cur=connect.cursor()
except sql.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)

def reset():
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("CREATE TABLE Users(Username TEXT, Password TEXT)")

def authUser(username):
    ans = False;
    cur = sql.connect('userdata.db')
    data = cur.execute("SELECT rowid FROM users WHERE username = ?", (username,))
    data=data.fetchall()
    if len(data) != 0:
        ans = True
    return ans

def authLogin(username, password):
    ans = False
    if authUser(username):
        cur = sql.connect('userdata.db')
        data = cur.execute("SELECT password FROM users WHERE username = ? and password = ?", (username,password))
        if len(data.fetchall()) != 0:
            ans = True
    return ans

def register(username, password):
    #sanitize inputs here
    with connect:
        cur.execute("SELECT * from Users WHERE Username = '%s'" %username)
        row = cur.fetchall()
        print row
        if row == []:
            cur.execute("INSERT INTO Users VALUES ('"+username +"','"+password+"');")
            connect.commit()
#reset()
register("jyin", "password")
register("kevin", "password")
if connect:
    connect.close()
