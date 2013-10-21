
from pymongo import MongoClient
client = MongoClient()
users = client.db.users

def addUser(usrn, pswd):
    users.insert{'username':usrn,'password':pswd}

def authenticate(usrn, pswd):
    if users.find({'username':usrn}).count() == 0: return False
    dbEntry = users.find({'username':usrn})
    u = dbEntry['username']
    p = dbEntry['password']
    if u == None or p == None:
        return False
    elif p == pswd:
        return True
    else:
        return False



