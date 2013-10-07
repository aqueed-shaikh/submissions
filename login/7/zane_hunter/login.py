import sha
from flask.ext import shelve

secret = "uniquellama"
shelf = "thea"

def registerUser(usern, passw): 
	usern = usern.encode('ascii')
	passw = passw.encode('ascii')
	db = shelve.get_shelve('c')
	if not usern in db:
		hashpass = encrypt(passw)
		db[usern] = hashpass
		db.close()
		return True
	else:
		db.close()
		return False

def checkUser(app,usern,passw):
	db = shelve.get_shelve('c')
	hashpass = encrypt(passw)
	ans = db[usern] == hashpass
	shelve.close()
	return ans

def encrypt(passw):
	encrypter = sha.new(passw)
	encrypter.update(secret)
	hashpass = encrypter.digest()
	return hashpass
