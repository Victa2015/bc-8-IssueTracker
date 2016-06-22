from . import db, login_manager
from flask import current_app
# from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Department(db.Model):
    '''This class creates a department
    object.
    '''
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    dept_head = db.Column(db.Integer)

    from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from . import db, login_manager


class Comments(db.Model):
    '''This class creates comment objects
    associated with a user.
    '''

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',
                           backref=db.backref('comments', lazy='dynamic'))

class Issue(db.Model):
    '''This class creates issues objects
    by user object
    '''
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    description = db.Column(db.Text)
    priority = db.Column(db.String(10))
    closed = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User',
                           backref=db.backref('issues', lazy='dynamic'))

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department = db.relationship('Department',
                                 backref=db.backref('departments',
                                                    lazy='dynamic'))


class Role(db.Model):
    '''This class creates a User Role object
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    #is_admin = db.Column(db.Boolean, default = False)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    def __repr__(self):
        return '<User: %r>' % self.username




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
