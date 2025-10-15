import pytest
from app import create_app, db
from config import Config
from app.task.service import TaskService


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def task_service(app):
    return TaskService()


@pytest.fixture
def sample_tasks():
    return [
        dict(name="Task 1", description="Description for Task 1", priority="low"),
        dict(name="Task 2", description="Description for Task 2", priority="medium"),
        dict(name="Task 3", description="Description for Task 3", priority="high"),
    ]


def test_add_single_task(task_service, sample_tasks):
    task = task_service.create_task(**sample_tasks[0])
    tasks = task_service.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == task.id
    assert tasks[0].name == "Task 1"


def test_add_multiple_tasks(task_service, sample_tasks):
    for data in sample_tasks:
        task_service.create_task(**data)
    tasks = task_service.list_tasks()
    assert len(tasks) == 3
    assert [t.name for t in tasks] == ["Task 1", "Task 2", "Task 3"]


def test_delete_single_task(task_service, sample_tasks):
    task = task_service.create_task(**sample_tasks[0])
    tasks = task_service.list_tasks()
    assert len(tasks) == 1

    task_service.delete_task(task.id)
    with pytest.raises(ValueError):
        task_service.get_task(task.id)
    assert len(task_service.list_tasks()) == 0


def test_get_task_by_id(task_service, sample_tasks):
    task = task_service.create_task(**sample_tasks[0])
    found_task = task_service.get_task(task.id)
    assert found_task is not None
    assert found_task.id == task.id


def test_update_task_name(task_service):
    task = task_service.create_task(name="Task 1", description="Description for Task 1", priority=None)
    task.name = "Updated Task Name"
    db.session.commit()

    updated_task = task_service.get_task(task.id)
    assert updated_task.name == "Updated Task Name"
    assert updated_task.description == "Description for Task 1"


def test_update_task_description(task_service):
    task = task_service.create_task(name="Task 1", description="Description for Task 1", priority=None)
    task.description = "Updated Task Description"
    db.session.commit()

    updated_task = task_service.get_task(task.id)
    assert updated_task.name == "Task 1"
    assert updated_task.description == "Updated Task Description"


def test_delete_task_not_found(task_service):
    with pytest.raises(ValueError):
        task_service.delete_task(9999)


def test_get_task_not_found(task_service):
    with pytest.raises(ValueError):
        task_service.get_task(9999)

