from pymongo import MongoClient

def usedUsername(your_username):
    ans = False
    connection = MongoClient()
    db = connection['users']
    if(db.users.find({"username": "your_username"})
        ans = True
    return ans

def check(sql_database,username,password):
    ans = False
    if (usedUsername(sql_database,username)):
        logins = sqlite3.connect('SQL_users')
        checklogins = logins.execute('select * FROM users WHERE username = ? and password = ?', (username, password))
        if len(checklogins.fetchall()) != 0:
            ans = True
    return ans

def add(sql_database,username,password):
    logins = sqlite3.connect('SQL_users')
    logins.execute('insert into users(username,password) values(?,?)', (username,password))
    logins.commit()
    
        
