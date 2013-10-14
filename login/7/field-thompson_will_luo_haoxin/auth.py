import sqlite3

connection = sqlite3.connect("users.db")

q = "create table if not exists users(username TEXT, pw TEXT)"

connection.execute(q)
connection.commit()
connection.close()

def authenticate(username,pw):
    connection = sqlite3.connect("users.db")
    cursor = connection.execute("select pw from users where username = ?", [username])
    result = [line for line in cursor]
    result = line[0]
    if result == pw:
        return True
    return False

def add_user(username,pw):
    connection = sqlite3.connect("users.db")
    cursor = connection.execute("select username where username = ?",[username])
    result = [line for line in cursor]
    if len(result) != 0:
        return False #username already exists
    connection.execute("insert into users values(?,?)",[username],[pw])
    return True

