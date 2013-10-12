import sqlite3

class DatabaseObject(object):
  def __init__(self, data_file):
    self.db = sqlite3.connect(data_file, check_same_thread=False)
    self.data_file = data_file

  def write(self, query, values=None):
    cursor = self.db.cursor()
    if values is not None:
      cursor.execute(query, list(values))
    else:
      cursor.execute(query)
    self.db.commit()
    return cursor

  def read(self, query, values=None):
    cursor = self.db.cursor()
    if values is not None:
      print query, list(values)
      cursor.execute(query, list(values))
    else:
      cursor.execute(query)
    return cursor

  def drop_table(self, name):
    cursor = self.db.cursor()
    query = 'DROP TABLE %s' % name
    cursor.execute(query)
    self.db.commit()
    cursor.close()


class Table(DatabaseObject):
  def __init__(self, data_file, table_name, values):
    super(Table, self).__init__(data_file)
    cursor = self.db.cursor()
    query = 'CREATE TABLE IF NOT EXISTS %s%s' % (table_name, values)
    cursor.execute(query)
    self.db.commit()
    cursor.close()
    self.table_name = table_name

  def clear_entries(self):
    query = 'DELETE from %s' % self.table_name
    cursor = self.write(query)
    cursor.close()

  def destroy():
    self.drop_table(self.table_name)


class User(Table):
  def __init__(self, data_file):
    super(User, self).__init__(data_file, 'users', '(username TEXT, password TEXT)')
    
  def add_user(self, username, password):
    query = 'INSERT INTO users VALUES(?, ?)'
    cursor = self.write(query, [username, password])
    cursor.close()

  def exists(self, username):
    query = 'SELECT username FROM users WHERE username=?'
    cursor = self.read(query, [username])
    results = cursor.fetchall()
    cursor.close()
    return len(results) > 0

  def authenticate(self, username, password):
    query = 'SELECT password FROM users WHERE username=? and password=?'
    cursor = self.read(query, [username, password])
    results = cursor.fetchall()
    cursor.close()
    return len(results) > 0
