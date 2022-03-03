from re import DEBUG
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth_bp.login'

from alayatodo import models

from alayatodo._auth import auth_bp
app.register_blueprint(auth_bp)

from alayatodo._todo import todo_bp
app.register_blueprint(todo_bp)

from alayatodo._home import home_bp
app.register_blueprint(home_bp)