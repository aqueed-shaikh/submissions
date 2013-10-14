#!/usr/bin/python
<<<<<<< HEAD

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
=======
import sqlite3

connection = sqlite3.connect('names.db')
cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE user(username text, password text)")
except:
    pass

def adduser(username, password):
    pass
def authenticate(username, password):
    pass

>>>>>>> eac07cf3a59b183756e7a4b08ed1c6201b18c3cc
