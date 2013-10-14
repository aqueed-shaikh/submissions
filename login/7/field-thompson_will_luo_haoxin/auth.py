import sqlite3

connection = sqlite1.connection("users.db")

q = "create table users(username TEXT, pw TEXT)"

connection.execute(q)

def authenticate(username,pw):
    cursor = connection.execute("select pw from users where username = ?", [username])
    result = [line for line in cursor]
    result = line[0]
    if result == pw:
        return True
    return False

def addUser(username,pw):
    cursor = connection.execute("select username where username = ?",[username])
    result = [line for line in cursor]
    if len(result) != 0:
        return False //username already exists
    connection.execute("insert into users values(?,?)",[username],[pw])
    return True

    
