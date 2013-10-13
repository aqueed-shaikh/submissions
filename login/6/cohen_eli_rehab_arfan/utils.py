from flask import Flask
from flask import request, render_template, redirect, session, url_for
import sqlite3

def addUser(user, pword):
    data = sqlite3.connect('users.db')
    ul = data.execute("SELECT * FROM users WHERE username = '%s'" % user)
    result = []
    for line in ul:
        result.append(line)
    if result:
        return """Username exists in the database!"""        
    else:
        data.execute("INSERT INTO users VALUES ('%s','%s')" % (user, pword))
        session["username"] = user
    data.commit()

def checkUser(user, pword):
    data = sqlite3.connect('users.db')
    ul = data.execute("SELECT username FROM users")
    ulist = []
    for line in ul:
        ulist.append(line)
    pl = data.execute("SELECT password FROM users")
    plist = []
    for line in pl:
        plist.append(line)
    print (ulist)
    if ulist.count(user) == 0:
        return False
    elif plist[ulist.index(user)] != pword: 
        return False
    else:
        session["username"] = user
        return True
