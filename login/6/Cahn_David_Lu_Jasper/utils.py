from pymongo import MongoClient

def auth (user, passwd, coll):
    return [x for x in coll.find({'username': user, 'password': passwd})] != [] 

def addUser (user, passwd, coll):
    coll.insert({'username': user, 'password': passwd})
