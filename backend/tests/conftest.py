import pytest
from fastapi.testclient import TestClient
from app.main import create_app

@pytest.fixture
def client():
    with TestClient(create_app()) as value:
        yield value
