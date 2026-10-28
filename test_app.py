import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['application'] == "Menu-Driven Calculator API"

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_add_route(client):
    response = client.get('/add?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 15.0

def test_subtract_route(client):
    response = client.get('/subtract?num1=10&num2=5')
    assert response.status_code == 200
    assert response.get_json()['result'] == 5.0
