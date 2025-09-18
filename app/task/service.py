from .models import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1

    def create_task(self, name, description=None):
        task_id = str(self.next_task_id)

        if any(task.task_id == task_id for task in self.tasks):
            raise ValueError(f"Task with id '{task_id}' already exists")

        task = Task(task_id, name, description)
        self.tasks.append(task)
        self.next_task_id += 1
        return task

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        raise ValueError(f"Task with id '{task_id}' not found")

    def list_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.tasks.remove(task)

# create a test task service singleton to act as a mock db
# FIXME: Remove this after setting up a test db/real db objects
task_service = TaskService()