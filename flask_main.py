from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from model.fp_flask_sql import *
from flask_sqlalchemy import *

flask_app = Flask(__name__)
flask_app.debug = True

#
# BEGIN DATABASE SECTION #
#

flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes2.db'

db = SQLAlchemy(flask_app)

hero_user_table = db.Table('hero_user',
    db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    hero_user = db.relationship('User', secondary=hero_user_table, backref=db.backref('user', lazy='dynamic'))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
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

#This is how the values were added originally, but it crashes the app if you try to add them again.
if len(results) == 0:
    zagara = Hero(id = 1, name = 'Zagara')
    db.session.add(zagara)
    #db.session.delete(zagara)
    uther = Hero(id = 2, name = 'Uther')
    db.session.add(uther)
    #db.session.delete(uther)

    graymane = Hero(id = 3, name = 'Graymane')
    db.session.add(graymane)
    #db.session.delete(graymane)

    db.session.commit()

#
# END DATABASE SECTION
#



#@flask_app.route('/todo/<int:task_id>')
#def index(task_id):
#    return jsonify(greeting="<h1> Hello Task Id # {}  </h1>".format(task_id))

@flask_app.route("/")
def hello():
    return render_template("login.html")

@flask_app.route("/draft")
def render_a_template():
    return render_template('drafthelper.html', foo='')

# #@flask_app.route('/todo', methods = ['GET'])
# @flask_app.route('/heroes', methods = ['GET'])
# def get_all_heroes():
#     heroes = Hero.query.all()
#     reslist = []
#     for row in results:
#         reslist.append(dict(name=row.name))
#
#     print(reslist)
#     return jsonify(heroes=reslist)

if __name__ == '__main__':
    flask_app.run()

