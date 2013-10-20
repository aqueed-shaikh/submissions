from pymongo import MongoClient
c = MongoClient()
def authorize(username, password):
    return len(list(c.users.Collections.find({'username':username, 'password':password}))) == 1
def userExists(username):
    return len(list(c.users.Collections.find({'username':username}))) == 1
def createUser(username, password):
    if not userExists(username):
        c.users.Collections.insert({'username':username, 'password':password})
        return True
    else:
        return False
