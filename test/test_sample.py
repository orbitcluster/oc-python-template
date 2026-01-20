import pytest
from src.api.server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home route returns 200 and correct message."""
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["message"] == "Hello from the Flask Boilerplate Project!"


def test_health(client):
    """Test the health route."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
