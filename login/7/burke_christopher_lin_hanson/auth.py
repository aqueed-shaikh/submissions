import sqlite3


def adduser(username, password):
    connection = sqlite3.connect('test.db')
    q = "select * from logins where username='%s'"%(username)
    cursor = connection.execute(q)
    results = []
    for line in cursor:
        results.append(line)

    
    if len(results) == 0 :
        q = "insert into logins values ('%s','%s')"%(username,password)
        connection.execute(q)
        connection.commit()
        return True
    else :
        return False


def authenticate(username, password):
    connection = sqlite3.connect('test.db')
    q = "select password from logins where username='%s'"%(username)
    cursor = connection.execute(q)
    results = []
    for line in cursor:
        results.append(line)


    if len(results) > 0 and results[0][0] == password:
        return True
    else:
        return False
