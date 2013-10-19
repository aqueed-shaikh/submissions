from pymongo import MongoClient

def connect():
    conn = MongoClient()
    return conn

def login(username, password):
    if not username or not password:
        return "missing"
    with connect() as conn:
        login = conn.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if not r:
            return "no-user"
        if password != r["password"]:
            return "incorrect"

def register(username, password):
    if not username or not password:
        return "missing"
    with connect() as conn:
        login = conn.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if r:
            return "exists"
        login.insert({"username": username, "password": password})
