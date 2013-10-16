import sqlite3

def loginauth(username, password):
    c = sqlite3.connect('users.db')
    try:
        c.execute("SELECT * from users")
    except:
        return False
    try:
        r = c.execute("SELECT password FROM users WHERE username = ? and password = ?", [username,password])
        if len(r.fetchall()) == 0:
            return False
        return True
    except:
        return False

def regisauth(username, password):
    c = sqlite3.connect('users.db')
    try:
        c.execute("SELECT * from users")
    except:
        c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    r = c.execute("SELECT username FROM users WHERE username = ?", [username])
    if len(r.fetchall()) == 0:
        c.execute("INSERT INTO users VALUES (?, ?)", [username, password])
        return True
    return False
