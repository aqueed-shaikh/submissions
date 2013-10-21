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

def changepass(username, oldpass, newpass):
    if not username or not oldpass or not newpass:
        return "missing"
    with connect() as conn:
        login = conn.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if not r:
            return "no-user"
        if oldpass != r["password"]:
            return "incorrect"
        login.update({"username": username}, {"$set": {"password": newpass}})

def register(username, password):
    if not username or not password:
        return "missing"
    with connect() as conn:
        login = conn.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if r:
            return "exists"
        login.insert({"username": username, "password": password})
