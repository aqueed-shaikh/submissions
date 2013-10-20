from pymongo import MongoClient

def authenticate(username,pw):
    pass

def add_user(username,pw):
    client = MongoClient()
    db = client.users
    doc = {'username': username, 'pw': pw}
    db.pw.insert(doc)

def set_pass(username, pw):
    client = MongoClient()
    db = client.users
    db.pw.update({'username':username}, {"$set": {'pw':pw}}, upsert=False)
