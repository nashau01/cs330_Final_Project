from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model.fp_sql import *


app = Flask(__name__)
app.debug = True

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
    return jsonify(heroes=reslist)

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

