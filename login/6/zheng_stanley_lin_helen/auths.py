import sqlite3


def usernameExists(sql_database,username):
    ans = False
    logins = sqlite3.connect('SQL_users')
    checklogins = logins.execute('select * FROM users WHERE username = ?', (username,))
    if len(checklogins.fetchall()) != 0:
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
    
