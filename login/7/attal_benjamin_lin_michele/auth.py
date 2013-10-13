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
            cursor.execute(query, list(values))
        else:
            cursor.execute(query)
        return cursor

    def select(self, values, tables, **kwargs):
        vals = ','.join(values)
        locs = ','.join(tables)
        conds = ' and '.join(['%s=?' % k for k in kwargs])
        subs = [kwargs[k] for k in kwargs]
        query = 'SELECT %s FROM %s WHERE %s' % (vals, locs, conds)
        cursor = self.write(query, subs)
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
        query = 'CREATE TABLE IF NOT EXISTS %s%s' % (table_name, values)
        cursor = self.write(query)
        cursor.close()
        self.table_name = table_name

    def insert(self, *args):
        values = ','.join(['?' for l in args])
        query = 'INSERT INTO %s VALUES(%s)' % (self.table_name, values)
        cursor = self.write(query, args)
        cursor.close()

    def delete(self, **kwargs):
        conds = ' and '.join(['%s=?' % k for k in kwargs])
        subs = [kwargs[k] for k in kwargs]
        query = 'DELETE FROM %s where %s' % (self.table_name, conds)
        cursor = self.write(query, subs)
        cursor.close()

    def delete_all(self):
        query = 'DELETE from %s' % self.table_name
        cursor = self.write(query)
        cursor.close()

    def select(self, values, **kwargs):
        return super(Table, self).select(values, [self.table_name], **kwargs)

    def drop():
        self.drop_table(self.table_name)


class User(Table):


    def __init__(self, data_file):
        super(User, self).__init__(data_file, 'users', 
                                   '(username TEXT, password TEXT)')

    def exists(self, username):
        cursor = self.select(['username'], username=username)
        results = cursor.fetchall()
        cursor.close()
        return len(results) > 0

    def authenticate(self, username, password):
        cursor = self.select(['username'], username=username, 
                            password=password)
        results = cursor.fetchall()
        cursor.close()
        return len(results) > 0
