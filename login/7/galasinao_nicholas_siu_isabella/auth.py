#!/usr/bin/python
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

