from pymongo import MongoClient

def loginauth(username, password):
    #c = sqlite3.connect('users.db')
    connection = MongoClient()
    db = connection['users']
    try:
        db.users.find({'username':username}, {'password':password})
        return True
    except:
        return False

def regisauth(username, password):
    print username
    connection = MongoClient()
    try:
        db.users.find({'username':username})
        return False
    except:
        db.users.insert({'username':username}, {'password':password})
        return True
