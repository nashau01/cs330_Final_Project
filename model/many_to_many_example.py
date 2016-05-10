from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI='postgresql://username:password@localhost:5432/database'
db = SQLAlchemy(app)
relationship_table=db.Table('relationship_table',

                             db.Column('post_id', db.Integer,db.ForeignKey('posts.id'), nullable=False),
                             db.Column('tags_id',db.Integer,db.ForeignKey('tags.id'),nullable=False),
                             db.PrimaryKeyConstraint('post_id', 'tags_id') )

class Posts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255),nullable=False)
  content = db.Column(db.Text)
  tags=db.relationship('Tags', secondary=relationship_table, backref='posts' )

class Tags(db.Model):
     id=db.Column(db.Integer, primary_key=True)
     name=db.Column(db.String, unique=True, nullable=False)
     description=db.Column(db.Text)

"""
from flask_main import app
from flask_sqlalchemy import *

# from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy.orm import mapper
# from yourapplication.database import metadata, db_session

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes.db'

db = SQLAlchemy(app)

# relationship_table=db.Table('relationship_table',
#                              #db.Column('id', db.Integer, primary_key = True), #Is this line necessary?
#                              db.Column('hero_id', db.Integer, db.ForeignKey('hero.id'), nullable=False),
#                              db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
#                              db.PrimaryKeyConstraint('hero_id', 'user_id')
#                             )
#
# class HeroUser(db.Model):
#     __tablename__ = 'hero_user'
#     id = db.Column(db.Integer, primary_key = True)
#     db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False),
#     db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False),
#
#     # def __init__(self, id = None, hero_id = None, user_id = None):
#     #     self.id = None
#     #     self.hero_id = hero_id
#     #     self.user_id = user_id
#
# # users = Table('users', metadata,
# #     Column('id', Integer, primary_key=True),
# #     Column('name', String(50), unique=True),
# #     Column('email', String(120), unique=True)
# # )
#
# rt_class_mapping = mapper(HeroUser, relationship_table, non_primary = True)

class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # user=db.relationship('user', secondary=rt_class_mapping, backref='heroes' )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    #
    #Q: How is a many to many relationship betwen Hero and User accomplished in flask_sqlalchemy
    #
    #heroes_owned = db.Column(?) #Many
    #heroes_favorited = db.Column(?) #Many

db.create_all()


class HeroUser(db.Model):
    pass

results = db.session.query(Hero).all()

# This is how the values were added originally, but it crashes the app if you try to add them again.
if len(results) == 0:
    zagara = Hero(name = 'Zagara')
    db.session.add(zagara)
    uther = Hero(name = 'Uther')
    db.session.add(uther)
    graymane = Hero(name = 'Graymane')
    db.session.add(graymane)

    db.session.commit()

"""
