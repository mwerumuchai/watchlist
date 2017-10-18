from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing Flask extensions
    bootstrap.init_app(app)

    # registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    # We'll add the views and forms
    return app

# #initializing application
# app = Flask(__name__, instance_relative_config = True)
#
# # Setting up configurations
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")
#
# #initializing Flask extensions
# bootstrap = Bootstrap(app)
# from app import views
# from app import error
