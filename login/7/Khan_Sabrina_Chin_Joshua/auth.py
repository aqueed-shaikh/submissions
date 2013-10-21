import sqlite3

def get_connection():
    connection = sqlite3.connect("Usernames.db")
    connection.execute("create table if not exists Users(username TEXT, password TEXT)")
    connection.commit()
    return connection

def adduser(name, password):
    connection = get_connection()
    connection.execute("insert into Users VALUES('%s','%s')"%(name,password))
    connection.commit()

def authenticate(name, password):
    connection = get_connection()
    n = connection.execute("select Users.username from Users where Users.username = '%s'"%name)
    p = connection.execute("select Users.password from Users where Users.username = '%s'"%name)
    passwords = [item[0] for item in p]
    if (n == None or len(passwords) == 0):
        return False
    elif(passwords[0] == password):
        return True
    else:
        return False





