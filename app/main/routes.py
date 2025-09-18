from flask import render_template
from ..task.service import task_service

from app.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    user = {"username": "Chris"}
    #FIXME: Remove after deleting test data singleton in TaskService service.py
    for i in range(1, 4):
        task_service.create_task(f"task {i}", f"Task {i} test description")

    return render_template("index.html", title="Orbit Task Manager", user=user, tasks=task_service.list_tasks())
