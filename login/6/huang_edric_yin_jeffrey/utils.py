import pymongo
from pymongo import MongoClient

def authenticate(username, password):
    client = MongoClient()
    db = client['userdata']
    user = db.Users.find({ 'Username' : username })
    if user.count () == 0: #username is not found
        print "Username not found! Register first"
        return 1
    elif list(user)[0]["Password"] == password:
        print "This was a triumph."
        return 3
    else: #wrong password
        print "Wrong password."
        return 2

def register(username, password):
#sanitize inputs here
    if len(username) < 4:
        return 0
    if len(password) < 6:
        return 1
    
    client = MongoClient()
    db = client['userdata']
    user = db.Users.find({ 'Username':username})
    print user.count()
    if user.count() != 0:
        print "Username already exists"
        return 2
    else: 
        print "Success!"
        db.Users.insert({'Username' : username, 'Password' : password})

def changePassword(username,old,new):
    client = MongoClient()    
    db = client['userdata']
    if authenticate(username,old) == 3:
        print "kk"
        if len(new)<6:
            return 1
        db.Users.update({'Username':username},{'$set': {'Password':new}})
if __name__ == "__main__":
    register("jyin", "password")
    authenticate("jyin", "password")
    changePassword("jyin","password","lalalala")
    authenticate("jyin", "lalalala")
