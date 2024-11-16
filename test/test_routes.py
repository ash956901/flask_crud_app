import pytest
from app import create_app, mongo

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get("/api/users")
    assert response.status_code == 200

def test_create_user(client):
    payload = {"name": "John Doe", "email": "john@example.com", "password": "12345"}
    response = client.post("/api/users", json=payload)
    assert response.status_code == 201
