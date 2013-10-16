import sqlite3

def work():
    acc = sqlite3.connect('accounts.db')
    try:
        acc.execute("create table accounts(username text, password text)")
    except:
        pass
    return acc


def register(username,password):
    acc = work()
    acc.execute("insert into accounts(username, password) values(?,?)", [username,password]) 
    acc.commit()

def authenticate(username,password):
    acc = work()
    user = acc.execute("select username from accounts where username = ?", [username])
    user =  user.fetchone()[0]
    print username
    passw = acc.execute("select password from accounts where username = ?", [username])
    passw = passw.fetchone()[0]
    if username == user and password == passw:
        return True
    else:
        return False

