import sqlite3
c = sqlite3.connect("auth.db",check_same_thread=False)
def authorize(username, password):
    q = "SELECT * FROM users WHERE `username`='"+username+"' and `password`='"+password+"'"
    r = c.execute(q)
    for line in r:
        return True
    return False
def userExists(username):
    q = "SELECT * FROM users WHERE `username`='"+username+"'"
    r = c.execute(q)
    for line in r:
        return True
    return False                                                                                                       
def createUser(username, password):
    if not userExists(username):
    
        q = "SELECT `id` FROM users"
        r = c.execute(q)
        count = 1
        for line in r:
            count += 1
    
        q = "INSERT INTO users VALUES(%d,'%s','%s')"%(count,username,password)
        c.execute(q)
        return True
    else:
        return False

