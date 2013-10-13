import sqlite3

connection = sqlite3.connect("data.db", check_same_thread = False)

q = "create table data(username text, password text)"

try:
    connection.execute(q)
except:
    pass

def adduser(user, pw):
    if checkuser(user) ==False:
        connection.execute("INSERT INTO data (username, password) values (?,?);",user,pw)
        connection.commit()
def checkuser(user):
    ans = False
    d=connection.execute("SELECT username from data where username = (?)", user)
    d=d.fetchall()
    if len(d)!=0:
        ans=True
    return ans


def authenticate(user, pw):
    cursor = connection.execute("select password from data where username = ?", user)
    if cursor.fetchone()== pw:
        return True
    else:
        return False
