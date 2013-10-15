import sqlite3

connect = sqlite3.connect('data.db')

try:
    connect.execute("create table accounts(username text, password text)")
except:
    pass

def register(username,password):
    connect.execute('insert into accounts (username, password) values(?,?)', [username,password]) 
    connect.commit()

def authenticate(username,password):
    user = connect.execute('select username from accounts where username = ?', [username])
    
    passw = cursor.execute('select password from accounts where username = ?', [username])
    
    if username == user and password == passw:
        return True
    else:
        return False

