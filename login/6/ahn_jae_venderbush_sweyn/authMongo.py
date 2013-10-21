import pymongo
from pymongo import MongoClient
#db.createcollection("info")
#collection = db.collection_names()

def checkUsername(username):
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    ans = False; 
    if (db.info.find_one({'username':username})):
        return ans;
    else: 
        ans = True;
        return ans;

def checkLogin(username, password): 
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    ans = False;
    if checkUsername(username):
        if ((db.info.find({'username': username} , {"password" : password}))):
            ans = True;
            return ans;
        else: 
            return ans;
    else:
        return ans;

def addLogin(username, password): 
    client = MongoClient('db.stuycs.org')
    db=client.admin
    db.authenticate('softdev','softdev')
    if not checkUsername(username) and not checkLogin(username, password):
        db.info.insert ({'username':username}, {'password':password})
    
        
        
