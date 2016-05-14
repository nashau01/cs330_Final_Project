from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from model.fp_flask_sql import *
from flask_sqlalchemy import *
from controllers import forms
from model.heroes_graph import *

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

@flask_app.route("/register", methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm(request.form)

    return render_template('register.html', form=form)

@flask_app.route("/userProfile", methods=['GET', 'POST'])
def profile():

    print(request.data)

    login_form = forms.LoginForm(request.form)
    registration_form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and login_form.validate() and login_form.username.data != "":
        print("login form username: ", login_form.username.data)
        thisUser = db.session.query(User).filter_by(username=login_form.username.data).first()

        if thisUser == None:
            print("That username is not registered")
        else:
            if thisUser.password == login_form.password.data:
                #display thisUser's heroes
                displayHeroesForUser(thisUser)

    elif request.method=='POST' and registration_form.validate():
        newUser = User(username = registration_form.username.data, password = registration_form.password.data)

        added = tryAddingUserToDB(newUser)

        if added:
            # printDatabase()

            #allow them to choose their available heroes
            displayHeroSelector()

            #then display thisUser's heroes
            displayHeroesForUser()
        else:
            pass

    return render_template('userprofile.html')


@flask_app.route("/")
def login():
    form = forms.LoginForm(request.form)
    return render_template('login.html', form=form)

@flask_app.route("/draft", methods=['GET','POST'])
def render_a_template():
    form = forms.RegistrationForm(request.form)

    return render_template('drafthelper.html', foo='')

def displayHeroSelector():
    pass

def tryAddingUserToDB(in_username, in_password):
    user = User(username = in_username, password = in_password)
    if db.session.query(User).filter_by(username = in_username).first() != None:
        print("Database already contains that username")
        return False
    else:
        db.session.add(user)
        db.session.commit()
        return True

def tryAddingHeroToDB(in_hero_name):
    hero = Hero(name = in_hero_name)
    if db.session.query(Hero).filter_by(name = in_hero_name).first() != None:
        print("Database already contains that hero")
        return False
    else:
        db.session.add(hero)
        db.session.commit()
        return True

def addHeroForUser(in_hero_name, in_username):
    hero_entry = db.session.query(Hero).filter_by(name = in_hero_name)
    user_entry = db.session.query(User).filter_by(username = in_username)
    hero_entry.hero_user.append(user_entry)

def displayHeroesForUser(in_user):
    pass

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

    # DELETING FROM THE DATABASE
    # db.session.delete(post_results[0])
    # db.session.commit()

    # printDatabase()


def printDatabase():
    post_hero_query = db.session.query(Hero).all()
    post_user_query = db.session.query(User).all()

    # PRINTING DATABASE CONTENT

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



