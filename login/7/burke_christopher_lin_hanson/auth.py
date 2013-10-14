import sqlite3

connection = sqlite3.connect('test.db')


def adduser(username, password):
    
    q = "insert into logins values(username,password)"
    connection.execute(q)

def authenticate:
