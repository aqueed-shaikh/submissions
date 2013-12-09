from pymongo import MongoClient

def usedUsername(your_username):
    ans = False
    connection = MongoClient()
    db = connection['users']
    if(list(db.users.find({"username": your_username})).len != 0):
        ans = True
    return ans

def check(your_username, your_password):
    ans = False
    connection = MongoClient()
    db = connection['users']
    list = list(db.users.find({"username": your_username, "password": your_password}))
    if(list.len == 1):
       ans = True
    return ans

def add(your_username, your_password):
    connection = MongoClient()
    db = connection['users']
    db.users.insert({"username": your_username, "password": your_password})
    return True

def changepassword(your_username, old_password, new_password):
    connection = MongoClient()
    db = connection['users']
    if(check(your_username, old_password)):
        db.users.update({"password": new_password})
    return old_password
        
