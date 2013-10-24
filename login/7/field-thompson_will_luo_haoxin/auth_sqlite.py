import sqlite3

def connection():
    connection = sqlite3.connect("users.db")
    connection.execute("create table if not exists users(username TEXT, pw TEXT)")
    return connection

def authenticate(username,pw):
    connection = connection()
    cursor = connection.execute('select pw from users where username="%s"'%username)
    result = [line for line in cursor]
    if len(result) > 0 and result[0][0] == pw:
        return True
    return False

def add_user(username,pw):
    connection = connection()
    cursor = connection.execute('select username from users where username="%s"'%username)
    result = [line for line in cursor]
    if len(result) != 0:
        return False #username already exists
    connection.execute('insert into users values("%s","%s")'%(username,pw))
    connection.commit()
    connection.close()
    return True

