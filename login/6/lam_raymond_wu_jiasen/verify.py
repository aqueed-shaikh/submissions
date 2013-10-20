from pymongo import MongoClient

def add(user,pw):
	connection = MongoClient()
	db = connection['users']
	if (db.users.find({"user": user}, fields = {"_id": False})):
		pass
	else:
		db.users.insert({"user": user}, {"pw": pw})

def verify(user, pw):
	connection = MongoClient()
	db = connection['users']
	if (db.users.find({"user": user}, {"pw": pw})) :
		return True
	else:
		return False

def checkcopy(user):
	connection = MongoClient()
	db = connection['users']
	if (db.users.find({"user": user}, fields = {"_id": False})):
		return False
	else:
		return True