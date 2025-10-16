from .models import Task
from app import db


class TaskService:
    def create_task(self, name, description, priority=None, completed=False):
        task = Task(name=name, description=description, priority=priority, completed=completed)
        db.session.add(task)
        db.session.commit()
        return task

    def get_task(self, task_id):
        try:
            id = int(task_id)
        except (TypeError, ValueError):
            raise ValueError(f"Task with id '{task_id}' not found")

        task = db.session.get(Task, id)
        if task is None:
            raise ValueError(f"Task with id '{task_id}' not found")
        return task

    def list_tasks(self):
        return Task.query.all()

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        db.session.delete(task)
        db.session.commit()
        return True

    def toggle_task_completion(self, task_id):
        task = self.get_task(task_id)
        task.completed = not task.completed
        db.session.commit()
        return task

# module-level singleton used by routes and views
task_service = TaskService()
