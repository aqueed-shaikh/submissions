import sqlite3

def setup():
    c = sqlite3.connect('logins.db')
    c.execute('create table if not exists users(username TEXT, password TEXT, count INTEGER);')
    c.commit();

def addLogin(username, password):
    if checkUsername(username) == False:
        c = sqlite3.connect('logins.db')
        c.execute('insert into users(username, password, count) values(?, ?, 0);', (username, password))
        c.commit()

def checkUsername(username):
    ans = False;
    c = sqlite3.connect('logins.db')
    data = c.execute("SELECT rowid FROM users WHERE username = ?", (username,))
    data=data.fetchall()
    if len(data) != 0:
        ans = True
    return ans

def checkLogin(username, password):
    ans = False
    if checkUsername(username):
        c = sqlite3.connect('logins.db')
        data = c.execute("SELECT password FROM users WHERE username = ? and password = ?", (username,password))
        if len(data.fetchall()) != 0:
            ans = True
    return ans

def incrementCount(username):
    c = sqlite3.connect('logins.db')
    c.execute('UPDATE users SET count=count+1 WHERE username=?', (username,))
    c.commit()

def getCount(username):
    c = sqlite3.connect('logins.db')
    data = c.execute("SELECT count FROM users WHERE username = ?", (username,))
    data = data.fetchall()
    return data[0][0]

def main():
    #setup()
    addLogin('sweyn', 'test')
    incrementCount('sweyn');
    c = sqlite3.connect('logins.db')
    q = "select * from users;"
    result = c.execute(q)
    result = [x for x in result]
    for name in result:
        print name
    print checkUsername('sweyn')
    print checkUsername('dan')
    print checkLogin('sweyn','password')
    getCount('sweyn')
    c.execute('drop table users')

if __name__=="__main__":
    main()