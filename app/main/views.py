from . import main
from flask import render_template, redirect, request, url_for, flash, g
from flask_login import login_user, login_required, logout_user, current_user
from ..models import *
from .. import db
from .forms import IssueForm


@main.route('/', methods=['GET', 'POST'])
def index():

	return render_template('index.html')

@main.route('/new', methods=['GET', 'POST'])
@login_required
def newissue():
    form = IssueForm()
    if form.validate_on_submit():
        user = current_user.id
        issue_ = Issue(name=form.name.data,
                       description=form.description.data,
                       priority=form.priority.data,
                       user_id=user)
        # import ipdb; ipdb.set_trace()
        db.session.add(issue_)
        db.session.commit()
        flash('Issue posted successfully. We shall do our best to help you')
        return redirect(request.args.get('next') or url_for('main.index'))

    user = User.query.filter_by(id=current_user.id).first()
    issues_ = user.issues.all()
    closed_issues = 0
    open_issues = 0

    for i in issues_:
        if i.closed:
            closed_issues += 1
        else:
            open_issues += 1
    total_issues = closed_issues + open_issues
    return render_template('issue.html',
                           form=form, issues_=issues_,
                           total_issues=total_issues,
                           closed_issues=closed_issues,
                           open_issues=open_issues)

@main.route('/myissues', methods=['GET', 'POST'])
@login_required
def myissue():
	user = User.query.filter_by(id=current_user.id).first()
	issues_ = user.issues.all()
	closed_issues = 0
	open_issues = 0

	for i in issues_:
		if i.closed:
			closed_issues += 1
		else:
			open_issues += 1
	total_issues = closed_issues + open_issues
	return render_template('myissue.html',
                           issues_=issues_,
                           total_issues=total_issues,
                           closed_issues=closed_issues,
                           open_issues=open_issues)

@main.route('/issue/closed', methods=['GET', 'POST'])
@login_required
def closed():
    if request.method == 'POST':
        id_ = request.form.get('cl')
        issue = Issue.query.filter_by(id=id_).first()
        issue.closed = True
        db.session.add(issue)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('main.index'))
