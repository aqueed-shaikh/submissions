import sqlite3

def connect():
    conn = sqlite3.connect("login.db")
    try:
        conn.execute("SELECT 1 FROM login")
    except:
        conn.execute("CREATE TABLE login (username TEXT, password TEXT)")
    return conn

def login(username, password):
    if not username or not password:
        return "missing"
    conn = connect()
    r = conn.execute("SELECT username, password FROM login WHERE username = ?", [username])
    results = r.fetchall()
    if not results:
        return "no-user"
    if password != results[0][1]:
        return "incorrect"

def register(username, passwordd):
    if not username or not password:
        return "missing"
    conn = connect()
    r = conn.execute("SELECT username FROM login WHERE username = ?", [username])
    results = r.fetchall()
    if results:
        return "exists"
    conn.execute("INSERT INTO login VALUES (?, ?)", [username, password])
