import pytest
from app.task.models import Task

valid_name = "taskname"
valid_description = "null"
valid_completed_bool = False
valid_priority_strings = ["low", "medium", "high"]
valid_priority_none = None

invalid_name_too_long = "TooLongOfANameForTask"
invalid_description_too_long = "TooLongDescriptionForTaskThatIsInvalidBecauseItIsMoreThan50Characters"


@pytest.fixture
def valid_task():
    return Task(name=valid_name, description=valid_description, priority=valid_priority_none, completed=valid_completed_bool)


def test_valid_task_constructor(valid_task):
    assert valid_task.id is None  # not persisted yet
    assert valid_task.name == valid_name
    assert valid_task.description == valid_description
    assert valid_task.completed is False


def test_invalid_task_constructor_completed_not_bool():
    with pytest.raises(ValueError):
        Task(name=valid_name, description=valid_description, priority=valid_priority_none, completed=None)

def test_valid_set_name(valid_task):
    new_name = "NewName"
    valid_task.name = new_name
    assert valid_task.name == new_name


def test_valid_set_description(valid_task):
    new_description = "New description for the task."
    valid_task.description = new_description
    assert valid_task.description == new_description


def test_invalid_set_name_null(valid_task):
    with pytest.raises(ValueError):
        valid_task.name = None


def test_invalid_set_name_too_long(valid_task):
    with pytest.raises(ValueError):
        valid_task.name = invalid_name_too_long


def test_invalid_set_description_null(valid_task):
    with pytest.raises(ValueError):
        valid_task.description = None


def test_invalid_set_description_too_long(valid_task):
    with pytest.raises(ValueError):
        valid_task.description = invalid_description_too_long


def test_get_name(valid_task):
    assert valid_task.name == valid_name


def test_get_description(valid_task):
    assert valid_task.description == valid_description


def test_task_repr(valid_task):
    repr_str = valid_task.__repr__()
    assert "Task" in repr_str and valid_name in repr_str and valid_description in repr_str


def test_task_to_dict(valid_task):
    valid_task_dict = valid_task.to_dict()
    assert valid_task_dict == {'id': None, 'name': 'taskname', 'description': 'null', 'priority': None, 'completed': False}


def test_task_priority_none(valid_task):
    assert valid_task.priority is None


def test_task_priority_any(valid_task):
    assert valid_task.priority is None or valid_task.priority in valid_priority_strings


def test_task_priority_low():
    Task(name=valid_name, description=valid_description, priority="low", completed=valid_completed_bool)


def test_task_priority_medium():
    Task(name=valid_name, description=valid_description, priority="medium", completed=valid_completed_bool)


def test_task_priority_high():
    Task(name=valid_name, description=valid_description, priority="high", completed=valid_completed_bool)


def test_task_priority_invalid_input():
    with pytest.raises(ValueError):
        Task(name=valid_name, description=valid_description, priority="invalid", completed=valid_completed_bool)

