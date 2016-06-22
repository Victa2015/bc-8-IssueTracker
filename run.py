import os
from app import create_app, db
#from app.models import User, Document
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User

app = create_app(os.getenv('ISSUE_TRACKER_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import User, Document

    # migrate database to latest revision
    upgrade()

if __name__ == '__main__':
    manager.run()