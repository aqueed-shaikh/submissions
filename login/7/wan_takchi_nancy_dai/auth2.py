from pymongo import MongoClient

client = MongoClient()
db = client.database
db.login.insert({'user':'Admin', 'pass':'Admin'})

def register(user, pw):
    if checkuser(user) == False:
        db.login.insert({'user':user, 'pass':pw})
        return True
    
def checkuser(user):
    ans = False
    db.login.

def changePass(user, pw, npw):

def login(user, pw):
