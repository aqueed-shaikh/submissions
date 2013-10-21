from pymongo import MongoClient
client = MongoClient()
db = client.db

def authenticate(username,pw):
    l = [x for x in db.login.find({"username":username,"pw":pw})]
    return len(l) != 0

def add_user(username,pw):
    l = [x for x in db.login.find({"username":username})]
    if len(l) == 0:
        doc = {'username': username, 'pw': pw}
        db.login.insert(doc)
        return True
    return False


def set_pass(username, pw):
    db.login.update({'username':username}, {"$set": {'pw':pw}}, upsert=False)
    

