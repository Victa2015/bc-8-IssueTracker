from flask import render_template, redirect, request, url_for, flash, g
from flask_login import login_user, login_required, logout_user, current_user
from . import issue
from ..models import Issue
from .. import db



@issue.route('/issues')
@login_required
def view_issues():
    issues = Issue.query.all()
    if request.method == 'GET' and request.args.get('close'):
        issue_id = request.args.get('issue_id')
        # update the database
        issue = Issue.query.filter_by(id=issue_id).first()
        issue.closed = 1
        db.session.commit()
        flash("Issue Solved!")

    return render_template('viewissues.html', issues=issues)
