from pymongo import MongoClient

client = MongoClient()
db = client['logins']


def insert(username, password):
    db.users.insert({'username': username, 'password': password})


def exists(username):
    user = db.users.find({'username': username}, fields={'_id': False})
    return len([u for u in user]) > 0


def authenticate(username, password):
    user = db.users.find({'username': username, 'password': password},
        fields={'_id': False})
    return len([u for u in user]) > 0

def change(username, newpass):
    db.users.update({'username': username}, {'$set': {'password': newpass}})
