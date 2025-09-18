import pytest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True

@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app


@pytest.fixture
def client(app):
    return app.test_client()

def test_config(app):
    assert app.config["TESTING"] is True

def test_homepage(client):
    response = client.get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "<title>Orbit Task Manager</title>" in html
    assert "Task 1" in html
    assert "should not see" not in html


def test_taskpage(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert b"Task Page" in response.data
