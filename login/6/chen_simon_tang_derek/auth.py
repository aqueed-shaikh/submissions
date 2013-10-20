from flask import Flask
from flask import session, url_for, request, redirect, render_template
import sqlite3

def work():
    acc = sqlite3.connect('accounts.db')
    try:
        acc.execute("create table accounts(username text, password text, security text, answer text)")
    except:
        pass
    return acc


def register(username,password,security,answer):
    acc = work()
    chk = acc.execute("select username from accounts where username = ?", [username] )
    chk =  len(chk.fetchall())
    print chk
    if(chk == 0):
        acc.execute("insert into accounts(username, password,security,answer) values(?,?,?,?)", [username,password,security,answer]) 
        acc.commit()
        return True
    else:
        return False
   

def authenticate(username,password):
    acc = work()
    user = acc.execute("select username from accounts where username = ?", [username] )
    if(len(user.fetchall()) == 0):
        return False
    user = acc.execute("select username from accounts where username = ?", [username] )
    user =  user.fetchone()[0]
    print user
    passw = acc.execute("select password from accounts where username = ?", [username])
    passw = passw.fetchone()[0]
    if username == user and password == passw:
        return True
    else:
        return False

