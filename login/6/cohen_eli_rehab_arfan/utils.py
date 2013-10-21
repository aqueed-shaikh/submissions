from pymongo import MongoClient

connection = MongoClient()
db = connection['users']

def addUser(username, password, password2):
    if (db.users.find_one({'username': username}, fields = {'_id': False})):
        return "copy"
    elif (password.__len__() < 4):
        return "short"
    elif (password != password2):
        return "match"
    else:
        db.users.insert({'username': username, 'password': password})
        return "good"


def checkUser(username, password):
    for x in db.users.find({'username': username, 'password': password}):
        return True
    else:
        return False

def changePwd(username, password, password2):
    if (password.__len__() < 4):
        return "short"
    elif (password != password2):
        return "match"
    else:
        db.users.update(
            { 'username': username},
            { '$set': { 'password': password} },
            #{ multi: true }
            )
        return "good"  
