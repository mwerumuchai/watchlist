from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
# from flask.ext.bootstrap import Bootstrap


login_manager =LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail=Mail()

#upload photos
photos = UploadSet('photos', IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    #creating MAIL
    mail.init_app(app)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing Flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # registering the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    #configure UploadSet
    configure_uploads(app,photos)

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
