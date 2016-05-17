from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# from model.fp_flask_sql import *
from flask_sqlalchemy import *
from controllers import forms
from heroes_graph import *
from heroes_graph import all_heroes
from fp_draft_helper import HoTS_Drafter

flask_app = Flask(__name__)
flask_app.debug = True

draft_dict = {
    "allies" : [],
    "enemies" : [],
    "user_owned_heroes" : []
}

#
# BEGIN DATABASE SECTION #
#
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes4.db'

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

@flask_app.route("/registering", methods=['POST'])
def registerUser():
    registration_form = forms.RegistrationForm(request.form)
    if request.method == 'POST' and registration_form.validate():
        newUser = User(username=registration_form.username.data, password=registration_form.password.data)

        added = tryAddingUserToDB(newUser)

        if added:
            # printDatabase()

            # allow them to choose their available heroes
            displayHeroSelector()

            # then display thisUser's heroes
        else:
            return render_template('username_taken.html')

        return redirect("/userProfile")

    return redirect("/")


@flask_app.route("/userProfile", methods=['GET', 'POST'])
def profile():
    login_form = forms.LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        print("login form username: ", login_form.username.data)
        thisUser = db.session.query(User).filter_by(username=login_form.username.data).first()

        if thisUser is None:
            return render_template('login_fail.html')
        else:
            if thisUser.password == login_form.password.data:
                global currentUser
                currentUser = login_form.username.data
                #display thisUser's heroes
                return redirect("/draft")

    if not currentUser == "":
        return render_template("userprofile.html", username=currentUser)

    return redirect('/')

@flask_app.route('/addHero/<string:in_username>/<string:in_hero_name>', methods = ['GET'])
def addHeroFor(in_username, in_hero_name):

    hero_entry = db.session.query(Hero).filter_by(name = in_hero_name).first()
    user_entry = db.session.query(User).filter_by(username = in_username).first()

    print(hero_entry, user_entry)

    hero_entry.hero_user.append(user_entry)

    db.session.commit()

    hero_list = []
    for a_hero in user_entry.hero_user:
        hero_list.append(a_hero.name)

    return redirect("/userProfile")


@flask_app.route("/getHeroes/<string:in_username>", methods = ['GET'])
def displayHeroesForUser(in_username):
    user = db.session.query(User).filter_by(username = in_username).first()
    heroes = user.hero_user
    #hero_name_list = []
    hero_name_dict = {}
    for a_hero in heroes:
        hero_name_dict[a_hero.name] = a_hero.name

    #return jsonify({'heroes': hero_name_list})
    return jsonify(hero_name_dict)

@flask_app.route("/addAlly/<string:in_hero_name>", methods = ['GET', 'PUT'])
def addAlly(in_hero_name):
    draft_dict['allies'].append(in_hero_name)
    print(draft_dict['allies'])
    return displayOptimalSelections()

@flask_app.route("/addEnemy/<string:in_hero_name>", methods = ['GET'])
def addEnemy(in_hero_name):
    draft_dict['enemies'].append(in_hero_name)
    return displayOptimalSelections()

@flask_app.route("/")
def login():
    form = forms.LoginForm(request.form)
    printDatabase()
    return render_template('login.html', form=form)


@flask_app.route("/draft", methods=['GET','POST'])
def render_a_template():
    form = forms.RegistrationForm(request.form)
    printDatabase()
    #tryAddingHeroToDB("Uther")
    #addHeroFor("Evan12", "Uther")

    return render_template('drafthelper.html', username=currentUser)

@flask_app.route("/displayOptimalSelections", methods = ['GET'])
def displayOptimalSelections():
    drafter = HoTS_Drafter(draft_dict['allies'], draft_dict['enemies'], draft_dict['user_owned_heroes'])
    print(drafter.ordered_optimal_selections)

    number_of_options_returned = 5

    #keys: (int) rank    values: (string) name
    opt_selections_dict = {}

    for i in range(number_of_options_returned):
        rank_int = i + 1
        rank_key = str(rank_int)
        opt_selections_dict[rank_key] = drafter.ordered_optimal_selections[i][0]

    # return render_template("optimal_selections.html", ordered_optimal_selections = drafter.ordered_optimal_selections)
    print(opt_selections_dict)

    return jsonify(opt_selections_dict)

def displayHeroSelector():
    pass

def tryAddingUserToDB(in_user):
    if db.session.query(User).filter_by(username = in_user.username).first() != None:
        return False
    else:
        db.session.add(in_user)
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

    if len(pre_hero_query) == 0:

        ### CREATING HEROES
        zagara = Hero(id = 1, name = 'Zagara')
        uther = Hero(id = 2, name = 'Uther')
        graymane = Hero(id = 3, name = 'Graymane')

        db.session.add(graymane)
        db.session.add(uther)
        db.session.add(zagara)

        ### CREATING USERS
        bob = User(id = 1, username = "bobby")
        sarah = User(id = 2, username = "sarah")
        chris = User(id = 3, username = "chrissy")

        db.session.add(bob)
        db.session.add(sarah)
        db.session.add(chris)

        ### ADDING TO THE DATABASE
        # graymane = db.session.query(Hero).filter_by(name = 'Graymane').first()
        sarah = db.session.query(User).filter_by(username = 'sarah').first()
        sarah.hero_user.append(graymane)
        sarah.hero_user.append(zagara)
        sarah.hero_user.append(uther)
        # bob.hero_user.append(db.session.query(Hero).filter_by(name = 'Zagara').first())

        db.session.commit()

        ### DELETING FROM THE DATABASE
        # db.session.delete(post_results[0])
        # db.session.commit()

def addAllHeroesToDB():
    for i in range(len(all_heroes)):
        hero = Hero(id = i, name = all_heroes[i])
        db.session.add(hero)
        db.session.commit()

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
            print("   ", a_hero.name)

def clearDatabase():
    users = User.query.all()
    for u in users:
        db.session.delete(u)

    heroes = Hero.query.all()
    for h in heroes:
        db.session.delete(h)

    db.session.commit()


if __name__ == '__main__':

    currentUser = ""
    # print(all_heroes)

    #testDatabase()
    # printDatabase()

    if (len(db.session.query(Hero).all()) == 0):
        addAllHeroesToDB()
    # printDatabase()

    # clearDatabase()

    flask_app.run()




