import sqlite3

SQL_Users = sqlite3.connect("SQL_Users")
CREATE TABLE users(username TEXT, password TEXT)
