import sqlite3

def init_auth(app):
	create_db()

def create_db():
	con = sqlite3.connect('sqldata.db')
	with con:
		con.cursor().execute('CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)')

def get_users():
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT * FROM Users')
	return cur.fetchall()

def get_users_as_list():
	users = get_users()
	return ['|'.join(str(i) for i in user) for user in users]

def create_user(username, password):
	con = sqlite3.connect('sqldata.db')
	with con:
		cur = con.cursor()
		cur.execute('INSERT INTO Users(username, password) VALUES("%s", "%s")' % (username, password))

def update_user(username, password):
	con = sqlite3.connect('sqldata.db')
	with con:
		cur = con.cursor()
		cur.execute('UPDATE Users SET password="%s" WHERE username="%s"'%(password, username))

def username_exists(username):
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT password FROM Users WHERE username = "%s" LIMIT 1' % username)
	return cur.fetchone() != None

def validate_user(username, password):
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT password FROM Users WHERE username = "%s" LIMIT 1' % username)
	p = cur.fetchone()
	return p != None and p[0] == password

def print_tables():
	cur = sqlite3.connect('sqldata.db').cursor()
	cur.execute('SELECT name FROM sqlite_master WHERE type="table"')
	print cur.fetchall()
