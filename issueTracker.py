import os
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'issuetracker2.db')
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Play with the dogs.",
                           text="Some text here.")


@app.route('/add', methods=['GET', 'POST'])
def add():


    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
