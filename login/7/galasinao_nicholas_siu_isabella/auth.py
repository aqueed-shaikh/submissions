#!/usr/bin/python

import sqlite3

database = sqlite3.connect('names.db', check_same_thread = False)

try:
    database.execute('''
    CREATE TABLE if not exists user(username text, password text)
''')
    database.commit()
except:
    pass

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
    
    database.commit()
    if len(u1.fetchall()) != 0:
        ans = True
    return ans

def authenticate(username,password):
    u1=database.execute('''
SELECT username FROM user WHERE username={}
'''.format(username))
    
    if len(u1.fetchall()) != 0:
        return True
    else:
        return False

