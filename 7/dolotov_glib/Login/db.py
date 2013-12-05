from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

connection = MongoClient()
dbase = connection.database
collection = dbase.collection

def add(uname,pword):
    collection.insert({uname:pword})


def login(uname,pword):
    if collection.find_one({uname:pword}):
        return True
    return False
