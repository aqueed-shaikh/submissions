import sqlite3

conn = sqlite3.connect('puppies.db')
c = conn.cursor()

try: 
    c.execute(""" CREATE TABLE users (username text, password text) """)
    c.commit();
except:
    pass

def adduser(username, password):
    try:
        c.execute(""" INSERT INTO users VALUES (?,?) """, (username, password))
        c.commit()
        return True
    except:
        return False


def autheticate(username, password):
    try:
        c.execute(""" SELECT username FROM users WHERE username=? AND password=? """, (username,password))
        print c.fetchone()
    except:
        pass
