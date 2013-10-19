from pymongo import MongoClient

def loginauth(username, password):
    c = MongoClient()
    db = c['logindb']
    try:
        db.users.find({'username':username, 'password':password})
        return True
    except:
        return False

def regisauth(username, password):
    c = MongoClient()
    db = c['logindb']
    try:
        db.users.find({'username':username})
        return False
    except:
        db.users.insert({'username':username, 'password':password})
        return True

