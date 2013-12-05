from pymongo import MongoClient

def init_auth(app):
	pass

def get_collection(): 
	client = MongoClient()
	db = client.login.users
	return db

def get_users_as_list():
	return [u.username + "|" + u.pword for u in get_collection().users.find()]

def create_user(username, password):
	get_collection().insert({'username': username, 'pword': password})

def update_user(username, password):
	if username_exists(username):
		get_collection().update({'username':username}, {"$set": {'pword':password}}, upsert=False)

def username_exists(username):
	l = [u for u in get_collection().find({'username':username})]
	return len(l) != 0

def validate_user(username, password):
	l = [u for u in get_collection().find({'username':username, 'pword':password})]
	return len(l) == 1
