import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_phase3_select(client):
    rv = client.get('/phase3/')
    assert rv.status_code == 200
