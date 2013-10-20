from pymongo import MongoClient

client = MongoClient()
db = client.database
db.login.insert({'user':'Admin', 'pass':'Admin'})

def register(user, pw):
    if checkuser(user) == False:
        db.login.insert({'user':user, 'pass':pw})
        return True
    
def checkuser(user):
    try:
        db.login.find({'user':user}) #don't allow same username
        return True
    except: 
        return False

def changePass(user, pw, npw):
    if login(user,pw):
        db.login.update({'user':user}, {$set: {'pass':npw}})
    
def login(user, pw):
    try
        db.login.find({'user':user, 'pass':pw})
        return True
    except: 
        return False
