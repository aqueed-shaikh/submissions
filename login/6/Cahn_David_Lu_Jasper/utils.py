import sqlite3

def userNameExist (sql_database,username):
    ans = 0
    db = sqlite3.connect ('SQL_Users')
    dbcheck = db.execute ('select * FROM users WHERE username = ?', (username,))
    if len (dbcheck.fetchall()) != 0:
        ans = 1

    if ans == 0:
        print 'user does not exist'
    else:
        print 'user exists'
    return ans;

def authenticate (sql_database, username, password):
    ans = 0
    if (userNameExist (sql_database,username)== 1):
        db = sqlite3.connect ('SQL_Users')
        dbcheck = db.execute ('select * FROM users WHERE username = ? and password = ?', (username,password))

        if len(dbcheck.fetchall()) != 0:
            ans = 1
    print 'authentication compelete'
    return ans

def addUser (sql_database, username, password):
    db = sqlite3.connect ('SQL_Users')
    db.execute('insert into users(username, password) values(?, ?)', (username, password))
    db.commit()
    print 'user added'




    
