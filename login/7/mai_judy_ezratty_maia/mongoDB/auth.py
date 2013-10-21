#Judy Mai & Maia Ezratty 

from pymongo import MongoClient

connection = MongoClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')

def adduser(username, password):
    db.users.insert({'username': username, 'password': password})

def authenticate(username, password):
    user = db.users.find({'username': username, 'password': password},
        fields={'_id': False})
    return len([u for u in user]) > 0

def changepw(username, oldpw, newpw):
    user = db.users.find({'username': username, 'password': oldpw},
        fields={'_id': False})
    if len([u for u in users]) == 0:
        return false
    else:
        db.users.update({'username': username}, {'$set': {'password': newpw}})
	
