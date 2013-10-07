import sha
from flask.ext import shelve

secret = "uniquellama"
shelf = "thea"

def registerUser(app, usern, passw): 
	shelve.init_app(app)
	db = shelve.get_shelve(shelf)
	hashpass = encrypt(passw)
	db[usern] = hashpass
	shelve.close()
def checkUser(app,usern,passw):
	shelve.init_app(app)
	db = shelve.get_shelve(shelf)
	hashpass = encrypt(passw)
	ans = db[usern] == hashpass
	shelve.close()
	return ans
def encrypt(passw):
	encrypter = sha.new(passw)
	encrypter.update(secret)
	hashpass = encrypter.digest()
	return hashpass
