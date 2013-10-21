from pymongo import MongoClient

connection = MongoClient()
db = connection['users']

def checkuser(username, password):
    if (db.users.find_one({"username": username}, fields ={"_id": False})):
        return 0
    else:
        return 1
        
    

def adduser(username, password):
    if not (db.users.find_one({"username": username}, fields ={"_id": False})):
        db.users.insert({'username': username, 'password' : password})
        return 0
    else:
        return 1
