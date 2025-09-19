import pytest
from app.task.models import Task

valid_task_id = "1"
valid_name = "taskname"
valid_description = "null"
valid_completed_bool = False

invalid_task_id_too_long = "12345678901"
invalid_task_id_null = None
invalid_name_too_long = "TooLongOfANameForTask"
invalid_description_too_long = "TooLongDescriptionForTaskThatIsInvalidBecauseItIsMoreThan50Characters"


@pytest.fixture
def valid_task():
    return Task(valid_task_id, valid_name, valid_description, valid_completed_bool)


def test_valid_task_constructor(valid_task):
    assert valid_task.task_id == valid_task_id
    assert valid_task.name == valid_name
    assert valid_task.description == valid_description
    assert valid_task.completed is False


def test_invalid_task_constructor_task_id_too_long():
    with pytest.raises(ValueError):
        Task(invalid_task_id_too_long, valid_name, valid_description)


def test_invalid_task_constructor_task_id_null():
    with pytest.raises(ValueError):
        Task(invalid_task_id_null, valid_name, valid_description)

def test_invalid_task_constructor_completed_not_bool():
    with pytest.raises(ValueError):
        Task(valid_task_id, valid_name, valid_description, None)

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


def test_get_task_id(valid_task):
    assert valid_task.task_id == valid_task_id


def test_get_name(valid_task):
    assert valid_task.name == valid_name


def test_get_description(valid_task):
    assert valid_task.description == valid_description


def test_task_id_immutable(valid_task):
    with pytest.raises(AttributeError):
        valid_task.task_id = "new_id"

def test_task_repr(valid_task):
    assert  f"<Task {valid_task_id} Name: {valid_name} Description: {valid_description}> Completed: {valid_completed_bool}" == valid_task.__repr__()

def test_task_to_dict(valid_task):
    valid_task_dict = valid_task.to_dict()

    assert valid_task_dict == {'id': '1', 'name': 'taskname', 'description': 'null', 'completed': False}
                               
                               # '')