# Separate out funcitonality in here
# Use sqlite as database
import sqlite3

db = sqlite3.connect('login')
command = 'create table users(username TEXT, password TEXT)'
db.execute(command)

def addUser(username, password):
  cmd = 'insert into users values("%s", "%s")' % (username, password)
  db.execute(cmd)

def exists(username):
  cmd = 'select password from users where username="%s"' % username
  cursor = db.execute(cmd)
  results = [line for line in cursor]
  return len(results) > 0

def authenticate(username, password):
  cmd = 'select password from users where username="%s"' % username
  cursor = db.execute(cmd)
  results = [line for line in cursor]
  return password in results
