import sha
from flask.ext import shelve

secret = "uniquellama"
shelf = "thea"

def registerUser(app, usern, passw): 
	shelve.init_app(app)
	db = shelve.get_shelve(shelf)
	hashpass = encrypt(passw)
	db[usern] = hashpass
	
def checkUser(app,usern,passw):
	shelve.init_app(app)
	db = shelve.get_shelve(shelf)
	hashpass = encrypt(passw)
	return db[usern] == hashpass
def encrypt(passw):
	encrypter = sha.new(passw)
	encrypter.update(secret)
	hashpass = encrypter.digest()
	return hashpass
