from pymongo import MongoClient

def connect():
    con = MongoClient()
    return con

def login(username, password):
    if !username || !password:
        return "missing"
    with connect() as con:
        login = con.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if not r:
            return "notfound"
        if password != r["password"]:
            return "incorrect"

def register(username, password):
    if !username || !password:
        return "missing"
    with connect() as con:
        login = con.login.login
        r = login.find_one({"username": username}, fields={"_id": False})
        if r:
            return "exists"
        login.insert({"username": username, "password": password})
