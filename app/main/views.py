from . import main
from flask import render_template
from flask import render_template, redirect, request, url_for, flash, g
from flask_login import login_user, login_required, logout_user, current_user
from ..models import User
from .. import db
from .forms import IssueForm


@main.route('/', methods=['GET', 'POST'])
def index():
	form = IssueForm()
	return render_template('index.html', form = form)
