import sqlite3

connection = sqlite3.connect("Usernames.db")

def adduser(name, password):
    connection.execute("insert into Usernames VALUES('%s','s')",name,password)

def authenticate(name, password):
    n = ("select Username.username from Users where Usernames.username = '%s'", name)
    p = ("select Username.password from Users where Usernames.username = '%s'", name)
    if (n == None):
        return False
    elif(p == password):
        return True
    else:
        return False





