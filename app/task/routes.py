from flask import request, jsonify
from app.task import bp
from app.task.service import task_service

@bp.route("/", methods=["GET"])
def list_tasks():
    tasks = [
        {"id": t.task_id, "name": t.name, "description": t.description, "priority": t.priority, "completed": t.completed}
        for t in task_service.list_tasks()
    ]
    return jsonify(tasks)

@bp.route("/", methods=["POST"])
def create_task():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    priority = data.get("priority")
    completed = data.get("completed", False)

    if not name:
        return jsonify({"success": False, "error": "Task name required"}), 400

    task = task_service.create_task(name, description, priority, completed)
    return jsonify({
        "success": True,
        "task": {"id": task.task_id, "name": task.name, "description": task.description, "priority": task.priority, "completed": task.completed},
    })

@bp.route("/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        task_service.delete_task(task_id)
        return jsonify({"success": True})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 404


@bp.route("/<task_id>/toggle_complete", methods=["PATCH"])
def toggle_task(task_id):
    try:
        task = task_service.toggle_task_completion(task_id)
        return jsonify({
            "success": True,
            "task": {"id": task.task_id, "name": task.name, "description": task.description, "completed": task.completed}
        })
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 404
