from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model.fp_flask_sql import *

flask_app = Flask(__name__)
flask_app.debug = True

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

