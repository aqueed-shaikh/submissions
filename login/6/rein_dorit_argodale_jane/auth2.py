from pymongo import MongoClient

def usedUsername(your_username):
    ans = False
    connection = MongoClient()
    db = connection['users']
    if(db.users.find({"username": your_username})
        ans = True
    return ans

def check(your_username, your_password):
    ans = False
    connection = MongoClient()
    db = connection['users']
    list = list(db.users.find({"username": your_username, "password": your_password}))
    if(list.len == 1)
       return ans


    
        
