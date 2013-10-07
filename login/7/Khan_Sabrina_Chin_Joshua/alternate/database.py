__author__ = "Joshua Chin"

from flask import escape
from flask.ext.sqlalchemy import SQLAlchemy

class Database:

    def __init__(self, app, directory):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+directory
        db = SQLAlchemy(app)
        class User(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(100), unique=True)
            password = db.Column(db.String(100), unique=True)

            def __init__(self, username, password):
                self.username = escape(username)
                self.password = escape(password)

            def __repr__(self):
                return '<User %r>' % self.username
        self.db = db
        self.User = User

    def create_all(self):
        self.db.create_all()

    def register(self, username, password):
        user = self.User(username, password)
        self.db.session.add(user)
        self.db.session.commit()

    def users(self):
        return self.User.query.all()

    def find_user(self, username):
        return self.User.query.filter_by(username=username).first()

    def is_user(self, username):
        return bool(find_user(username))
