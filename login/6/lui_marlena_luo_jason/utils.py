from pymongo import MongoClient

def connect():
    connection = MongoClient()
    return connection

def checkuser(username, password):
    ans = 0;
    a = login.find_one({"username": username}, fields ={"_id": False})
    if not a:
        ans = 1

    if password != a["password"]:
        ans = 2

    return ans

def adduser(username, password):
    ans = True
    a = login.find_one({"username": username}, fields ={"_id": False})
    if a:
       ans = False
    login.insert({"username": username, "password": password})
    return ans
