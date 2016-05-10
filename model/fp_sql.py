from flask_main import app
from flask_sqlalchemy import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes.db'

db = SQLAlchemy(app)

class Hero(db.Model):
    __tablename__ = 'hero'
    name = db.Column(db.String, primary_key=True)

class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    #
    #Q: How is a many to many relationship betwen Hero and User accomplished in flask_sqlalchemy
    #
    #heroes_owned = db.Column(?) #Many
    #heroes_favorited = db.Column(?) #Many

db.create_all()


"""
class HeroUser(db.Model):
    ?
"""

results = db.session.query(Hero).all()

# This is how the values were added originally, but it crashes the app if you try to add them again.
#if len(results) == 0:
# zagara = Hero(name = 'Zagara')
# db.session.add(zagara)
# uther = Hero(name = 'Uther')
# db.session.add(uther)
# graymane = Hero(name = 'Graymane')
# db.session.add(graymane)
#
# db.session.commit()
