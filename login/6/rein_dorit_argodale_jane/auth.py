import sqlite3

def usedUsername(sql_database,username):
    ans = false
    logins = sqlite3.connect('SQL_users')
    checklogins = logins.execute('select * FROM users WHERE username = ?', (username))
    if len(allusernames.fetchall()) != 0:
        ans = true

def check(sql_database,username,password):
    ans = false
    if (usedUsername(sql_database,username)):
        logins = sqlite3.connect('SQL_users')
        checklogins = logins.execute('select * FROM users WHERE username = ? and password = ?' (username, password))
        if len(checklogins.fetchall()) != 0:
            ans = true
    return ans

def add(sql_database,username,password):
    logins = sqlite3.connect('SQL_users')
    logins.execute('insert into users(username,password) values(?,?)' (username,password))
    logins.commit()
    
        
