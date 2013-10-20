from pymongo import MongoClient

connection = MongoClient()
db = connection['users']

def addUser(username, password):
    if (db.users.find_one({"username": username}, fields = {"_id": False})):
        return "Username and password already exists. Please try again."
    else:
        db.users.insert({"username":username, "password":password})


def checkUser(username, password):
    if (db.users.find({'username':username}, {'password':password})):
        return True
    else:
        return False
    
        
