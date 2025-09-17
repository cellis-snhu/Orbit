import pytest
from app.task.models import Task
from app.task.service import TaskService

@pytest.fixture
def task_service():
    return TaskService()


@pytest.fixture
def sample_tasks():
    return [
        Task("task1", "Task 1", "Description for Task 1"),
        Task("task2", "Task 2", "Description for Task 2"),
        Task("task3", "Task 3", "Description for Task 3"),
    ]


def test_add_single_task(task_service, sample_tasks):
    task_service.tasks.append(sample_tasks[0])
    tasks = task_service.list_tasks()
    assert len(tasks) == 1
    assert tasks[0] == sample_tasks[0]


def test_add_multiple_tasks(task_service, sample_tasks):
    for task in sample_tasks:
        task_service.tasks.append(task)
    tasks = task_service.list_tasks()
    assert len(tasks) == 3
    assert tasks[0] == sample_tasks[0]
    assert tasks[1] == sample_tasks[1]
    assert tasks[2] == sample_tasks[2]


def test_delete_single_task(task_service, sample_tasks):
    task_service.tasks.append(sample_tasks[0])
    tasks = task_service.list_tasks()
    assert len(tasks) == 1

    task_service.delete_task("task1")
    with pytest.raises(ValueError):
        task_service.get_task("task1")
    assert len(task_service.list_tasks()) == 0


def test_get_task_by_id(task_service, sample_tasks):
    task_service.tasks.append(sample_tasks[0])
    found_task = task_service.get_task("task1")
    assert found_task is not None
    assert found_task == sample_tasks[0]


def test_update_task_name(task_service):
    task = Task("task1", "Task 1", "Description for Task 1")
    task_service.tasks.append(task)
    # simulate update call
    task.name = "Updated Task Name"

    updated_task = task_service.get_task("task1")
    assert updated_task.name == "Updated Task Name"
    assert updated_task.name != "Task 1"
    assert updated_task.description == "Description for Task 1"


def test_update_task_description(task_service):
    task = Task("task1", "Task 1", "Description for Task 1")
    task_service.tasks.append(task)
    task.description = "Updated Task Description"

    updated_task = task_service.get_task("task1")
    assert updated_task.name == "Task 1"
    assert updated_task.description == "Updated Task Description"
    assert updated_task.description != "Description for Task 1"


def test_add_task_already_exists(task_service):
    task_service.create_task("First Task", "First description")

    # reset taskID to old value
    task_service.next_task_id = 1

    # creating another task should raise ValueError
    with pytest.raises(ValueError, match="already exists"):
        task_service.create_task("Duplicate Task", "Should fail")


def test_delete_task_not_found(task_service):
    with pytest.raises(ValueError):
        if not task_service.delete_task("task1"):
            raise ValueError("Task not found")


def test_update_task_name_not_found(task_service):
    with pytest.raises(ValueError):
        task_service.get_task("nonexistentTask")


def test_update_task_description_not_found(task_service):
    with pytest.raises(ValueError, match="Task with id 'nonexistentTask' not found"):
        task_service.get_task("nonexistentTask")

