from .models import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_task_id = 1

    def create_task(self, name, description=None, priority=None, completed=False):
        task_id = str(self.next_task_id)

        if any(task.task_id == task_id for task in self.tasks):
            raise ValueError(f"Task with id '{task_id}' already exists")

        task = Task(task_id, name, description, priority, completed)
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
task_service.create_task("Get milk", "Go to the store for milk", "low", False)
task_service.create_task("Study Chemistry", "Study for chemistry test", None, False)
task_service.create_task("Practice Guitar", "Spend an hour playing guitar", "high", False)
task_service.create_task("Clean Room", "Tidy up bedroom and organize desk", "medium", False)
task_service.create_task("Read Book", "Read 30 pages of a novel", None, False)
task_service.create_task("Exercise", "Go for a 30-minute run", "high", False)
task_service.create_task("Call Mom", "Check in with mom and chat", "low", False)
task_service.create_task("Write Journal", "Reflect on today's events", None, False)
task_service.create_task("Grocery Shopping", "Buy vegetables and fruits", "medium", False)
task_service.create_task("Finish Report", "Complete work report before deadline", "high", False)
task_service.create_task("Meditate", "Spend 15 minutes meditating", "low", False)
task_service.create_task("Water Plants", "Water all indoor plants", None, False)
task_service.create_task("Plan Trip", "Research destinations and flights", "medium", False)
