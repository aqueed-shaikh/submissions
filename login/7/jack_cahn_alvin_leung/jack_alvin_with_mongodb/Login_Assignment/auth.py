#!/usr/bin/python
#!flask/bin/python

#This is Jack Cahn and Alvin Leung's Project

import sqlite3
connection = sqlite3.connect('test.db', check_same_thread = False)

def adduser(username,password): 
    if authenticateRegister(username): 
        return False
    else: 
        q = 'INSERT INTO logins VALUES("%(username)s","%(password)s")';
        d = {'username': username,
             'password': password}
        connection.execute(q%(d))
        return True; 

def authenticate(username,password):
    ans = False
    authen = """
  select logins.username from logins where logins.username = "%(user)s" and logins.password = "%(password)s"
    """

    d = { 
        'user' : username, 
        'password' : password}
    
    cursor = connection.execute(authen%(d))
    return len(cursor.fetchall()) != 0

def authenticateRegister(username):
    ans = False
    authen2 = """
    select logins.username from logins where logins.username = "%(user)s"
    """
    d = {'user' : username}
    print authen2%(d)
    
    cursor = connection.execute(authen2%(d))
    return len(cursor.fetchall()) != 0

