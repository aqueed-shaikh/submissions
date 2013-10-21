
from pymongo import MongoClient
connection = MongClient('db.stuycs.org')
db=connection.admin
db.authenticate('softdev','softdev')
