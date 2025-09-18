from flask import Flask
from app.task.service import TaskService
from app.task.service import task_service


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.update(
            TESTING=True,
        )

    from app.main import bp as main_bp
    from app.task import bp as task_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(task_bp)

    return app
