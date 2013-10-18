from pymongo import MongoClient

def connect():
    conn = MongoClient()
    return conn

def login(username, password):
    if not username or not password:
        return "missing"
    with connect() as conn:
        r = conn.login.login.findone({"username": username}, fields={"_id": False})
        if not r:
            return "no-user"
        if password != r["password"]:
            return "incorrect"

def register(username, password):
    if not username or not password:
        return "missing"
    with connect() as conn:
        r = conn.login.login.findone({"username": username}, fields={"_id": False})
        if r:
            return "exists"
        conn.login.login.insert({"username": username, "password": password})
