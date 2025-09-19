from flask import render_template
from ..task.service import task_service

from app.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    user = {"username": "Chris"}
    tasks = task_service.list_tasks()
    return render_template("index.html", title="Orbit Task Manager", user=user, tasks=tasks)

