from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Blog

app = create_app('production')

manage = Manager(app)
migrate = Migrate(app, db)

manage.add_command('server', Server)
manage.add_command('db', MigrateCommand)


@manage.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manage.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog)

if __name__ == '__main__':
    manage.run()