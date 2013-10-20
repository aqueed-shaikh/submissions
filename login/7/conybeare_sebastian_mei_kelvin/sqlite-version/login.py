import sqlite3

def login(uname, pword):
	connection = sqlite3.connect('users.db')

	q = """
	select users.username from users;
	"""
	cursor1 = connection.execute(q)
	names = [line for line in cursor1]
	
	p = """
	select users.password from users;
	"""
	cursor2 = connection.execute(p)
	passes = [line for line in cursor2]

	for i,val in enumerate(names):
		print names[i]
		print passes[i]
		if names[i][0] == uname and passes[i][0] == pword:
			return True
		return False

def register(uname, pword):	
	connection = sqlite3.connect('users.db')
	q = """
	select users.username from users;
	"""

	cursor1 = connection.execute(q)
	names = [line for line in cursor1]

	print names
	
	if uname in names:
		return False
	connection.execute('INSERT INTO users VALUES(?,?)', (uname,pword,))
	connection.commit()
	return True
