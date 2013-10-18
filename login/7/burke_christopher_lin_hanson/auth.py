import sqlite3
from pymongo import MongoClient

client = MongoClient()
db = client.newdb
db.newcollection


def adduser(username, password):
    #connection = sqlite3.connect('test.db')
    #q = "select * from logins where username='%s'"%(username)
    #cursor = connection.execute(q)
    #results = []
    #for line in cursor:
    #    results.append(line)

    
    #if len(results) == 0 :
    #    q = "insert into logins values ('%s','%s')"%(username,password)
    #    connection.execute(q)
    #    connection.commit()
    #    return True
    #else :
    #    return False
    copy = [x for x in db.newcollection.find({'username':username})]
    if len(copy) == 0:
        db.newcollection.insert({'username':username,'password':password})
        return True
    else:
        return False


def authenticate(username, password):
    connection = sqlite3.connect('test.db')
    q = "select password from logins where username='%s'"%(username)
    cursor = connection.execute(q)
    results = []
    for line in cursor:
        results.append(line)


    if len(results) > 0 and results[0][0] == password:
        return True
    else:
        return False
