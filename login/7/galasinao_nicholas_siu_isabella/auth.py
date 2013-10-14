#!/usr/bin/python

import sqlite3

connection = sqlite3.connect('names.db')
connection.execute('''
CREATE TABLE user
(username text, password text, log int)
''')

def adduser(username,password):
    connection.execute('''
INSERT INTO user VALUES({0},{1})
'''.format(username,password))
    
    connection.commit()

def authenticate(username,password):
    u1=connection.execute('''
SELECT username FROM user WHERE username={0}
'''.format(username))
    
    p1=cursor.execute('''
SELECT password FROM user WHERE username={0}
'''.format(username)))
    
    if username==u1 and password==p1:
        return True
    else:
        return False
