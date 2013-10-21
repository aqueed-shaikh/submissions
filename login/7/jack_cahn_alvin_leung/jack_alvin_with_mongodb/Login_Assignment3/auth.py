#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

from pymongo import MongoClient
connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

def adduser(username,password): 
    if authenticateRegister(username): 
        return False
    else: 
        db.JackAlvin.insert({'username':username,'password':password})
        return True; 

def authenticate(username,password):
    users = db.JackAlvin.find({'username':username,'password':password},
                              fields={'_id':False})
    return len([user for user in users]) != 0

def authenticateRegister(username):
    users = db.JackAlvin.find({'username':username},
                                             fields={'_id':False})
    return len([user for user in users]) != 0
def changepw(username,oldpw,newpw):
    users = db.JackAlvin.find({'username':username,'password':oldpw},
                              fields={'_id':False})

    if (len([user for user in users]) == 0):
        return false
    else: 
        db.JackAlvin.remove({'username':username,'password':oldpw})
        db.JackAlvin.insert({'username':username,'password':newpw})
        return True
