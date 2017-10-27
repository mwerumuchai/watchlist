# from app import app
from app import create_app,db
from flask_script import Manager, Server
from app.models import User,Role,Review
from flask_migrate import Migrate, MigrateCommand


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

#Migration
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

# Running Unittest
@manager.command
def test():
    '''
    Run the Unittest
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)

if __name__ == '__main__':
    manager.run()
