import sqlite3

def loginauth(username, password):
    c = sqlite3.connect('users.db')
    try:
        r = c.execute("SELECT password FROM users WHERE username = ? and password = ?", (username,password))
        if len(r.fetchall()) == 0:
            return False
        return True
    except:
        return False

def regisauth(username, password):
    c = sqlite3.connect('users.db')
    r = c.execute("SELECT username FROM login WHERE username = ?", (username))
    if len(r.fetchall()) == 0:
        c.execute("INSERT INTO login VALUES (?, ?)", (username, password))
        return True
    else:
        return False
