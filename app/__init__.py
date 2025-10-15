from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'main.login'

    from app.main import bp as main_bp
    from app.task import bp as task_bp

    from app import models

    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp, url_prefix="/tasks")

    return app
