from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#initializing application
app = Flask(__name__, instance_relative_config = True)

# Setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

#initializing Flask extensions
bootstrap = Bootstrap(app)
from app import views
