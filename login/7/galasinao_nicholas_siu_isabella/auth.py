#!/usr/bin/python

import sqlite3

def adduser(username,password):
    database = sqlite3.connect('names.db')
    database.execute('''
INSERT INTO user VALUES({},{})
'''.format(username,password))
    
    database.commit()

def exists(username):
    ans = False
    database = sqlite3.connect('names.db')
    u1 = database.execute('''
SELECT * FROM user WHERE username={}
'''.format(username))
    
    if len(u1.fetchall()) != 0:
        ans = True
    return ans

def authenticate(username,password):
    database = sqlite3.connect('names.db')
    u1=database.execute('''
SELECT username FROM user WHERE username={}
'''.format(username))
    
    p1=database.execute('''
SELECT password FROM user WHERE username={}
'''.format(username))
    
    if username==u1 and password==p1:
        return True
    else:
        return False

