from flask_main import app
from flask_sqlalchemy import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes.db'

db = SQLAlchemy(app)
db.create_all()

class Hero(db.Model):
    __tablename__ = 'hero'
    name = db.Column(db.String, primary_key=True)

    #id = db.Column(db.Integer, primary_key=True)
    #task = db.Column(db.String)
    #priority = db.Column(db.String)
    #due = db.Column(db.Date)
    #done = db.Column(db.Boolean)

    """
    class User(db.Model):
        __tablename__ = 'user'
        username = db.Column(db.String, primary_key=True)
        heroes_owned = db.Column(?) #Many
        heroes_favorited = db.Column(?) #Many
    """

    """
    class HeroUser(db.Model):
        ?
    """

results = db.session.query(Hero).all()

if len(results) == 0:
    zagara = Hero(name = 'Zagara')
    db.session.add(zagara)
    uther = Hero(name = 'Uther')
    db.session.add(uther)

    db.session.commit()
