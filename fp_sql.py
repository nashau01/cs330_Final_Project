from flask import Flask, request, jsonify, render_template
import os
from flask_sqlalchemy import SQLAlchemy

from datetime import date

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes.db'
db = SQLAlchemy(app)

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

db.create_all()

results = db.session.query(Hero).all()

if len(results) == 0:
    zagara = Hero(name = 'Zagara')
    db.session.add(zagara)
    uther = Hero(name = 'Uther')
    db.session.add(uther)

    db.session.commit()


#Some of the code below still needs to be tranlated in flask-sqlalchemy

#@app.route('/todo/<int:task_id>')
#def index(task_id):
#    return jsonify(greeting="<h1> Hello Task Id # {}  </h1>".format(task_id))

#@app.route('/todo', methods = ['GET'])
@app.route('/heroes', methods = ['GET'])
def get_all_tasks():
    #Session = sessionmaker(bind=engine)
    #Session.configure()
    #session = Session()
    #results = Todo.query.filter_by(done=False).all()
    heroes = Hero.query.all()
    reslist = []
    for row in results:
        #reslist.append(dict(id=row.id, task=row.task, priority=row.priority, due = row.due.isoformat()))
        reslist.append(dict(name=row.name))

    print(reslist)
    return jsonify(tasklist=reslist)

"""
@app.route('/todo/<int:task_id>', methods = ['PUT'])
def todo_one(task_id):
    Session = sessionmaker(bind=engine)
    Session.configure()
    session = Session()
    print(request.json)
    row = Todo.query.filter_by(id=task_id).update(dict(done=True))
    session.commit()
    return "done"
"""

if __name__ == '__main__':
    app.run()