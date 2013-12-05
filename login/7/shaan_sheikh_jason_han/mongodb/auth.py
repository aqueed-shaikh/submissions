import pymongo

from pymongo import mongoClient
client = MongoClient()

db = client.test_database

def authenticate(ID,PW):
    n = db.posts.find_one({id: ID})
    if n == []:
        return -2
    else:
        n = db.posts.find_one({id: ID},{pw: PW}) 
        if n == []:
            return -1
        else:
            return 0

def add_user(ID,PW):
    n = db.posts.find_one({id: ID})
    if n != []:
        return -1
    else:
        db.posts.save({id: ID},{pw: PW})
        return 0

