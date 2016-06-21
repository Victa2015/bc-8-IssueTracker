from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.mail import Mail
from flask_oauthlib.client import OAuth

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
db = SQLAlchemy()
moment = Moment()
mail = Mail()

oauth = OAuth()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'issuetracker2.db')
	app.config['SECRET_KEY'] = 'M*\xc7\xf0\x82\xe9\xe0\xa2]_\xca5V\xc3\x0b\xcd\x99\xe2\x90\xd0\x12\x92\xc4\xb8'
	db = SQLAlchemy(app)
	Bootstrap(app)
	return app


    

