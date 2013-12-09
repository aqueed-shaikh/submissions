from pymongo import MongoClient

client = MongoClient()
db = client.logins


def adduser(username, password):
    copy = [x for x in db.accounts.find({'username':username})]
    if len(copy) == 0:
        db.accounts.insert({'username':username,'password':password})
        return True
    else:
        return False


def authenticate(username, password):
    user = [x['password'] for x in db.accounts.find({'username':username})]

    if len(user) > 0 and user[0] == password:
        return True
    else:
        return False
