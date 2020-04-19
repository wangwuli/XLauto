#!/usr/bin/env python

# import os
# from main import create_app, db
# from main.models import User, Role
# from flask.ext.script import Manager, Shell
# from flask.ext.migrate import Migrate, MigrateCommand
#
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# manager = Manager(app)
# migrate = Migrate(app, db)
#
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command("shell", Shell(make_context=make_shell_context()))
# manager.add_command('db', MigrateCommand)
#
# if __name__ == '__main__':
#     manager.run()

from main import create_app
#import os
#config_name = os.environ.get('FLASK_CONFIG') or 'default'

if __name__ == '__main__':
    from flask_script import Manager
    manager = Manager(create_app())
    manager.run()