from pymongo import MongoClient

def start():
    c = MongoClient()
    db = c["userlogin"]
    logins = db["logins"]

def usernameExists(user):
    ans = False
    c = MongoClient()
    db = c["logins"]
    users = db["users"]
    if db.logins.find({'user': user}, fields = {'_id': False}).count() > 0:
        ans = True
    return ans

def check(username,password):
    ans = False
    c = MongoClient()
    db = c["logins"]
    users = db["users"]
    if db.logins.find({'user': username, 'password': password}).count() > 0:
        ans = True
    return ans

def changePass(username,password,newpassword):
    if check(username,password):
        db.logins.update({'user':username} {password = newpassword})

def add(username,password):
    c = MongoClient()
    db = c["logins"]
    db.logins.insert('user' : username,'password' : password)



    
