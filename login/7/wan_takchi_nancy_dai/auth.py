import sqlite3

connection = sqlite3.connect("data.db", check_same_thread = False)

q = "create table data(username text, password text)"

try:
    connection.execute(q)
except:
    pass

def adduser(user, pw):
    cursor = connection.execute("select username from data");
    for username in cursor:
        if username == user:
            return False
        else:
            connection.execute("INSERT INTO data VALUES('%s', '%s')"%(user, pw))
            return True

def authenticate(user, pw):
    cursor = connection.execute("select password from data where username = ?", user)
    if cursor.fetchone()== pw:
        return True
    else:
        return False
