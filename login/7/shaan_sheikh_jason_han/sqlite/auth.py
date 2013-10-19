import sqlite3



def adduser(ID, PW):
    connection = sqlite3.connection("session.db")

    p = ("select * from stuff where ID = %s", ID)
    cursor = connection.execute(p)
    if p != null:
        return 1
    
    q = ("insert into stuff(ID, PW) values('%s','%s')", ID, PW)
    cursor = connection.execute(q)
    connection.commit()
    return 0

def authenticate(ID, PW):
    connection = sqlite3.connection("session.db")

    p = ("select * from stuff where ID = %s", ID)
    cursor = connection.execute(p)
    if p == null:
        return 2

    q = ("select * from stuff where where ID = %s and PW = %s", ID, PW)
    cursor = connection.execute(q)
    if q == null:
        return 1
    
    return 0

