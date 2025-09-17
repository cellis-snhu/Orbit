from app.task import bp


@bp.route("/tasks")
def task():
    return "Task Page"
