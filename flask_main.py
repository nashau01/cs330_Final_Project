from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from model.fp_flask_sql import *
from flask_sqlalchemy import *
from controllers import forms

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

    #Extra: added for querying a user's heroes rather than just vise versa
    hero_user = db.relationship('Hero', secondary=hero_user_table, backref=db.backref('hero', lazy='dynamic'))


db.create_all()


"""
class HeroUser(db.Model):
    ?
"""

#
# END DATABASE SECTION
#


#@flask_app.route('/todo/<int:task_id>')
#def index(task_id):
#    return jsonify(greeting="<h1> Hello Task Id # {}  </h1>".format(task_id))

@flask_app.route("/")
def hello():
    return render_template("splashPage.html")

@flask_app.route("/register", methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)

    return render_template('register.html', form=form)

@flask_app.route("/login")
def login():
    return render_template('login.html')

@flask_app.route("/draft", methods=['POST'])
def render_a_template():
    username = request.form['username']
    password = request.form['password']


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

def testDatabase():
    pre_hero_query = db.session.query(Hero).all()

    # if len(pre_results) == 0:

    # CREATING HEROES
    # zagara = Hero(id = 1, name = 'Zagara')
    # uther = Hero(id = 2, name = 'Uther')
    # graymane = Hero(id = 3, name = 'Graymane')

    # CREATING USERS
    # bob = User(id = 1, username = "bobby")
    # sarah = User(id = 2, username = "sarah")
    # chris = User(id = 3, username = "chrissy")

    # ADDING TO THE DATABASE
    # graymane = db.session.query(Hero).filter_by(name = 'Graymane').first()
    # bob = db.session.query(User).filter_by(username = 'sarah').first()
    # bob.hero_user.append(graymane)
    # bob.hero_user.append(db.session.query(Hero).filter_by(name = 'Zagara').first())
    #
    # db.session.add(graymane)
    # db.session.add(bob)
    # db.session.commit()

    post_hero_query = db.session.query(Hero).all()
    post_user_query = db.session.query(User).all()

    # DELETING FROM THE DATABASE
    # db.session.delete(post_results[0])
    # db.session.commit()

    # PRINTING DATABASE CONTENT
    printing_database = False
    if (printing_database):
        for a_hero in post_hero_query:
            print(a_hero.name)
            print("   has users: ")
            for a_user in a_hero.hero_user:
                print("   ", a_user.username, "\n")
                # print("      has heroes: ")
                # for hero2 in a_user.hero_user:
                #     print("      ", hero2.name, "\n")

        for a_user in post_user_query:
            print(a_user.username)
            print("   has heroes: ")
            for a_hero in a_user.hero_user:
                print("   ", a_hero.name, "\n")

testDatabase()

if __name__ == '__main__':
    flask_app.run()



