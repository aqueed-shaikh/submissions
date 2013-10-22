import sha
import pymongo

secret_key = "uniquellama"
address = "localhost"
collection = "users"
database = "laurels"

def user(usern,passw = None):
	ans = {}
	if usern:
		ans["usern"] = usern
	if passw:
		ans["passw"] = passw
	return ans
def registerUser(usern, passw): 
	conn = pymongo.MongoClient(address);
	col = conn[database][collection]
	result = col.find_one(user(usern));
	if not result:
		col.insert(user(encrypt(usern),encrypt(passw)))
		return True

def checkUser(usern,passw):
	#passw = passw.encode('ascii')
	usern = encrypt(usern);
	passw = encrypt(passw);
	conn = pymongo.MongoClient(address);
	col = conn[database][collection]
	return col.find_one(user(usern,passw))
def encrypt(passw):
	encrypter = sha.new(passw)
	encrypter.update(secret_key)

	hashpass = encrypter.digest()

	return unicode(hashpass, errors='ignore') 
