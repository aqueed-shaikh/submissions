import sqlite3

connection = sqlite3.connect("data.db", check_same_thread = False)

q = "create table data(username text, password text)"

try:
    connection.execute(q)
except:
    pass

def adduser(user, pw):
    if checkuser(user) == False:
        connection.execute("INSERT INTO data (username, password) values (?, ?)", [user,pw])
        connection.commit()
        return True

def checkuser(user):
    ans = False
    d = connection.execute("SELECT username from data where username = ?", [user])
    d = d.fetchall()
    if len(d)!=0:
        ans = True
    return ans


def authenticate(user, pw):
    cursor = connection.execute("select password from data where username = ?", [user])
    result = (str)(cursor.fetchone())
    pw = "(u'" + pw + "',)"
    print result
    print pw
    if result == pw:
        return True
    else:
        return False
