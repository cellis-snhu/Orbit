from flask import Flask
from app.task.service import TaskService
from app.task.service import task_service
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from app.main import bp as main_bp
    from app.task import bp as task_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp, url_prefix="/tasks")

    return app
