import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Clear the in-memory data before each test
    from src.repositories.call_repository import CallRepository
    repo_instance = CallRepository()
    repo_instance._calls_data = [{

        "id": 1,    
        "caller": "Alice",
        "callee": "Bob",
        "timestamp": "2024-01-01T12:00:00Z",
        "is_archived": False
    },
    {
        "id": 2,
        "caller": "Charlie",
        "callee": "Dave",
        "timestamp": "2024-01-02T12:00:00Z",
        "is_archived": False
    }
    ]
    yield
   