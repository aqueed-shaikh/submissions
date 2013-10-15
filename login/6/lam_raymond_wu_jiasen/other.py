import sqlite3

connect = sqlite3.connect('data.db')
conn = connect.cursor()
try:
	conn.execute("create table users(un text, pw text")
except:
	pass

def add(user,pw):
	conn.execute("insert into users values('%s','%s')" % (user, pw))
	conn.commit()

def verify(user, pw):
	un = conn.execute("select un from users where un = '%s'" %user )
	pwd = conn.execute("select pw from users where un = '%s'", %user)
	if un == user and pwd == pw:
		return true
	else:
		return false

def checkcopy(user):
	check = conn.execute("select un from users where un = '%s'" %user)
	if check:
		return false
	else:
		return true