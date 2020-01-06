# define tables models

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP

from sqlalchemy.sql import func


db = SQLAlchemy()


class User(db.Model):
    """Model for the user table"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Post(db.Model):
    """Model for the post table"""
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(TIMESTAMP, nullable=False)


    def __init__(self, author_id, title, body):
        self.author_id = author_id
        self.title = title
        self.body = body
        self.created = func.now()


    def __repr__(self):
        return '<id {}>'.format(self.id)
