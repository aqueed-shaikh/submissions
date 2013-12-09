from pymongo import MongoClient
client = MongoClient()
db = client['doggies']

def adduser(username, password):
	litter = [puppy for puppy in db.puppies.find({'username':username})]
	if len(litter) == 0:
		db.puppies.insert({'username':username,'password':password})
		return True
	else:
		return False

def authenticate(username, password):
	litter = [puppy for puppy in db.puppies.find({'username':username})]
	if len(litter) == 0:
		return False
	else:
		return litter[0]['password'] == password

def changepass(username, old, new):
	if authenticate(username, old):
		db.puppies.update({'username':username}, {'$set':{'password':new}})
		return True
	else:
		return False
