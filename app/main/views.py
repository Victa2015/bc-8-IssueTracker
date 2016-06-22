from . import main
from flask import render_template, redirect, request, url_for, flash, g
from flask_login import login_user, login_required, logout_user, current_user
from ..models import User
from .. import db
from .forms import IssueForm


@main.route('/', methods=['GET', 'POST'])
def index():

	return render_template('index.html')

@main.route('/new', methods=['GET', 'POST'])
@login_required
def newissue():
	form = IssueForm()

	return render_template('issue.html', form = form)

@main.route('/myissues', methods=['GET', 'POST'])
@login_required
def myissue():
	return render_template('myissue.html')
