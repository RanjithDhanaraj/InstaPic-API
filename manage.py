# -*- coding: utf-8 -*-
import os
import unittest

from app.main.model import user

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

from app.main.model import blacklist

from app import blueprint

from add_to_db import add_users_and_posts

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def clear_db():
    """Clears the databse"""
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def fill_db():
    """add 3 sets of users and images to the database"""
    add_users_and_posts()


if __name__ == '__main__':
    manager.run()
