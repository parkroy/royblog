import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True

db = SQLAlchemy(app)
Migrate(app,db)

# export APP_SETTINGS="config.DevelopmentConfig"
# export DATABASE_URL="postgresql://localhost/royblog"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

#여기에 Blueprint 세팅
from royblog.core.views import core
from royblog.users.views import users
from royblog.blog_posts.views import blog_posts
from royblog.error_pages.handlers import error_pages

app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(core)
app.register_blueprint(error_pages)
