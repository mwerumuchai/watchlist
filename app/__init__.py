from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
# from flask.ext.bootstrap import Bootstrap


login_manager =LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail=Mail()
simple=SimpleMDE()

#upload photos
photos = UploadSet('photos', IMAGES)
def create_app(config_name):
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(__name__)
    app.config.from_object(config_options[config_name])

    #initializing Flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #create mail
    mail.init_app(app)
    #create simple review editor
    simple.init_app(app)

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
