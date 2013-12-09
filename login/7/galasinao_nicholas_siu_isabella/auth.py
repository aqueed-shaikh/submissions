#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient()
db = client.logins

def adduser(username,password):
    user = {'name':username, 'pw':password}
    db.logins.insert(user)

def exists(username):
    ans = False
    cursor = db.logins.find({'name':username})
    if cursor.count() > 0:
        ans = True
    return ans

def changePw(username, oldPw, newPw):
    db.logins.update({'name':username}, {'$set': {'pw':newPw}})

def authenticate(username,password):
    cursor = db.logins.find({'name':username,'pw':password})
    if cursor.count() > 0:
        return True
    else:
        return False

