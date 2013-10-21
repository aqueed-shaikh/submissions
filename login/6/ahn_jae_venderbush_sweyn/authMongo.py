from pymongo import MongoClient

def checkUsername(username):
    client = MongoClient()
    db=client.admin
    ans = False; 
    if (db.info.find_one({'username':username})):
        ans = True;
    return ans;

def checkLogin(username, password): 
    client = MongoClient()
    db=client.admin
    ans = False;
    if checkUsername(username):
        if ((db.info.find_one({'username': username} , {"password" : password}))):
            ans = True;
            return ans;
        else: 
            return ans;
    else:
        return ans;

def addLogin(username, password): 
    client = MongoClient()
    db=client.admin
    if not checkUsername(username) and not checkLogin(username, password):
        db.info.insert ({'username':username, 'password':password, 'count': 0})

        
def incrementCount(username):
    client = MongoClient()
    db=client.admin
    if checkUsername(username):
        account = db.info.find_one({'username':username})
        account['count'] = account['count'] + 1
        db.info.save(account)

def getCount(username):
    client = MongoClient()
    db=client.admin
    if checkUsername(username):
        account = db.info.find_one({'username':username})
        return account['count']

    
        
    
