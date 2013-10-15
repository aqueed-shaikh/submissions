import sqlite3


c=sqlite3.connect("auth.db")
c.execute("create table if not exists users(username TEXT, password TEXT);")
c.commit()
    
def validUsername(username):
    ret=True
    q="SELECT * FROM users WHERE 'username' = "+username
    r=c.execute(q)
    for line in r:
        ret=False
    return ret

def addUser(username,password):
    ret=False
    if validUsername(username):
        q="insert into users values(%s, %s)"%(username,password)
        c.execute(q)
        c.commit()
        ret=True
    return ret

def log(username,password):
    ret=False
    c=sqlite3.connect("auth.db")
    q="select * FROM users WHERE username = %s and password = %s"%(username,password)
    r=c.execute(q)
    for line in r:
        ret=True
    return ret
        
