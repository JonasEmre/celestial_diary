import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import timedelta

# App initialize and configs.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = "$2b$12$VnFBspLWLaMCWVh3YUkLPehT.MyWWlIw4L1gRmjZAfLEXsWZA/44G'"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)

# Objects for other packages.
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from celestial_application import routes
