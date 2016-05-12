

# from flask_main import flask_app
# from flask_sqlalchemy import *
#
# flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/heroes2.db'
#
# db = SQLAlchemy(flask_app)
#
# hero_user_table = db.Table('hero_user',
#     db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )
#
# class Hero(db.Model):
#     __tablename__ = 'hero'
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     hero_user = db.relationship('User', secondary=hero_user_table, backref=db.backref('user', lazy='dynamic'))
#
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String)
#     password = db.Column(db.String)
#
#     #
#     #Q: How is a many to many relationship betwen Hero and User accomplished in flask_sqlalchemy
#     #
#     #heroes_owned = db.Column(?) #Many
#     #heroes_favorited = db.Column(?) #Many
#
# db.create_all()
#
#
# """
# class HeroUser(db.Model):
#     ?
# """
#
# results = db.session.query(Hero).all()
#
# #This is how the values were added originally, but it crashes the app if you try to add them again.
# if len(results) == 0:
#     zagara = Hero(id = 1, name = 'Zagara')
#     db.session.add(zagara)
#     #db.session.delete(zagara)
#     uther = Hero(id = 2, name = 'Uther')
#     db.session.add(uther)
#     #db.session.delete(uther)
#
#     graymane = Hero(id = 3, name = 'Graymane')
#     db.session.add(graymane)
#     #db.session.delete(graymane)
#
#     db.session.commit()
#
#
