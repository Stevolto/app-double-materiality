import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_phase4_summary(client):
    rv = client.get('/phase4/')
    assert rv.status_code == 200
