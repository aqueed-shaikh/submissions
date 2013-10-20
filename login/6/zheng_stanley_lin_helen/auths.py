import sqlite3

def start():
    c = sqlite3.connect("logins.db")
    c.execute("create table if not exists users(username TEXT, password TEXT);")
    c.commit()

def usernameExists(user):
    ans = False
    c = sqlite3.connect("logins.db")
    q = "select * FROM users WHERE username = " + user
    r = c.execute(q)
    for line in r:
        ans = True
    return ans

def check(username,password):
    ans = False
    c = sqlite3.connect("logins.db")
    q = "select * FROM users WHERE username = %s and password = %s"%(username,password)
    r = c.execute(q)
    for line in r:
        ans = True
    return ans

def add(username,password):
    c = sqlite3.connect("logins.db")
    q = "insert into users values(%s,%s)"%(username,password)
    c.execute(q)
    c.commit()



    
