import pymongo
from pymongo import MongoClient
client = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')
c = client
c.createcollection("info")
#collection = db.collection_names()

def checkUsername(username):
    ans = False; 
    if ((c.info.find_one({'username':username}), fields = {"_id": False}))
        return ans;
    else 
        ans = true;
        return ans;

def checkLogin(username, password): 
    ans = False;
    if checkUsername(username):
        if ((c.info.find({'username': username} , {"password" : password}))):
            ans = True;
            return ans;
        else:
            return ans;

def addLogin(username, password): 
    if checkUsername(username) == False:
        c.info.insert ({'username':username}, {'password':password})
    else: 
        print 'try another username'
    
        
        
