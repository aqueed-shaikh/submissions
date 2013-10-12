# Separate out funcitonality in here
# Use sqlite as database
import sqlite3



def init():
  db = sqlite3.connect('login')
  cursor = db.cursor()
  command = 'CREATE TABLE IF NOT exists users(username TEXT, password TEXT)'
  cursor.execute(command)
  db.commit()
  db.close()

def add_user(username, password):
  db = sqlite3.connect('login')
  cursor = db.cursor()
  cmd = 'INSERT INTO users VALUES(?, ?)'
  cursor.execute(cmd, [username, password])
  db.commit()
  db.close()

def exists(username):
  db = sqlite3.connect('login')
  cursor = db.cursor()
  cmd = 'SELECT username FROM users WHERE username=?'
  results = [line for line in cursor.execute(cmd, [username])]
  return len(results) > 0

def authenticate(username, password):
  db = sqlite3.connect('login')
  cursor = db.cursor()
  cmd = 'SELECT password FROM users WHERE username=? and password=?'
  results = [line for line in cursor.execute(cmd, [username, password])]
  return len(results) > 0

def drop_TABLE():
  db = sqlite3.connect('login')
  cursor = db.cursor()
  cmd = 'DROP TABLE users'
  cursor.execute(cmd)
  db.commit()

init()
