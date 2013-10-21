from flask.ext import shelve
from flask.ext.shelve import get_shelve, init_app

def init_auth(app):
	app.config['SHELVE_FILENAME'] = 'shelvedata.db'
	init_app(app)

def create_db():
	pass

def get_users():
	return get_shelve('c')

def get_users_as_list():
	users = get_users()
	return [key + '|' + db[key] for key in users]

def create_user(username, password):
	get_shelve('c')[username] = password

def update_user(username, password):
	if username_exists(username):
		create_user(username, password)

def username_exists(username):
	return username in get_shelve('c')

def validate_user(username, password):
	db = get_shelve('c')
	return username in db and db[username] == password
