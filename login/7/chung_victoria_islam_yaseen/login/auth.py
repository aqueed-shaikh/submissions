import sqlite3

def add(username, password):
    connection = sqlite3.connect('daterbase.db')
    q = """
select * from login where username='%s'"%(username)
"""
    cursor = connection.execute(q)
    results = [line for line in cursor]
    if len(results) == 0:
        q = "insert into login values ('%s', '%s')"%(username, password)
        connection.execute(q)
        conneciton.commit()
        return True
    else:
        return False

        

def authenticate(username,password):
    connection = sqlite3.connect('daterbase.db')
    q = """
select password from login where username='%s'"%(username)
"""
    cursor = connection.execute(q)
    results = [line for line in cursor]
    if len(results) > 0 and results[0] == password:
        return True
    else:
        return False
        

        
