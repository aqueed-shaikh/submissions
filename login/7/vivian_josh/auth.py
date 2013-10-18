import sqlite3

c = sqlite3.connect('puppies.db',check_same_thread = False)
#c = conn.cursor()

try: 
    c.execute(""" CREATE TABLE users (username text, password text) """)
    c.commit();
except:
    pass

def adduser(username, password):
    x = c.execute (""" SELECT username FROM users WHERE username=? """,[username])
    if len(x.fetchall()) == 0:
        c.execute(""" INSERT INTO users(username,password) VALUES (?,?) """, [username, password])
        c.commit()
        return True
    else:
        return False


def autheticate(username, password):
    x = c.execute(""" SELECT username FROM users WHERE username=? AND password=? """, [username,password])
    if len(x.fetchall()) != 0:
        return True
    else:
        return False
