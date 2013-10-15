
import sqlite3

connection = sqlite3.connect("users.db")

def addUser(usrn, pswd):
    connection.execute("insert into usernames VALUES('%s','%s')", usrn, pswd)

def authenticate(usrn, pswd):
    u = ("select usernames.username from usernames where usernames.username = '%s'",usrn)
    p = ("select usernames.password from usernames where usernames.username = '%s'",usrn)
    if u == None or p == None:
        return False
    elif p == pswd:
        return True
    else:
        return False



