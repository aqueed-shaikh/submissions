#!/usr/bin/python

import pymongo

client = pymongo.MongoClient()

def adduser(username,password):
    database = client.userdb
    collection = database.usercol
    user = {name:username, pw:password}
    collection.insert(user)

def exists(username):
    ans = False
    database = client.userdb
    collection = database.usercol
    cursor = collection.find({name:username})

    if cursor.count() > 0:
        ans = True
    return ans

def changePw(oldPw, newPw):
    database = client.userdb
    collection = database.usercol
    collection.update({pw:oldPw}, {pw:newPw})

def authenticate(username,password):
    database = client.userdb
    collection = database.usercol
    cursor = collection.find({name:username,pw:password})
    
    if cursor.count() > 0:
        return True
    else:
        return False

