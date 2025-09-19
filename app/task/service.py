from .models import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1

    def create_task(self, name, description=None, completed=False):
        task_id = str(self.next_task_id)

        if any(task.task_id == task_id for task in self.tasks):
            raise ValueError(f"Task with id '{task_id}' already exists")

        task = Task(task_id, name, description, completed)
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

    def toggle_task_completion(self, task_id):
        task = self.get_task(task_id)
        task.completed = not task.completed
        return task

# create a test task service singleton to act as a mock db
# FIXME: Remove this after setting up a test db/real db objects
task_service = TaskService()

# sample tasks for testing
task_service.create_task("Get milk", "Go to the store for milk", False)
task_service.create_task("Study Chemistry", "Study for chemistry test", False)
task_service.create_task("Practice Guitar", "Spend an hour playing guitar", False)