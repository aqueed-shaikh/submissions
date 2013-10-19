#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

from pymongo import MongoClient

client = MongoClient()
db = client['jackalvinlogin']

def adduser(username,password): 
    if authenticateRegister(username): 
        return False
    else: 
        db.logins.insert({'username':username,
                          'password':password})
        return True; 

def authenticate(username,password):
    users = [user for user in db.logins.find({'username':username},
                                             fields={'_id':false,'user':True})
             if user['password'] == password]
    return len(users) != 0

def authenticateRegister(username):
    users = [user for user in db.logins.find({'username':username},
                                             fields={'_id':false,'user':True})]
    return len(users) != 0
def changepw(username,oldpw,newpw):
    return True #TODO: Write the change password code
