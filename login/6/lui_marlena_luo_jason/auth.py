import sqlite3

def setup():
    c = sqlite3.connect('users.db')
    c.execute('create table if not exists users(username TEXT, password TEXT)')
    c.commit;

def checkuser(username):
    ans = False;
    c = sqlite3.connect('users.db')
    data = c.execute("Select * from users WHERE username = ?", (username,))
    data = data.fetchall()
    if len(data) != 0:
        ans = True
    return ans

def adduser(username, password):
    if checkeruser (username) == False:
        c = sqlite3.connect('users.db')
        c.execute ('insert into users (username,password) values (?, ?)', (username password))
        c.commit()
        


    
