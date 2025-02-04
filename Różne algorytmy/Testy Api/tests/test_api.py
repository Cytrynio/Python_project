import pytest
from api.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient(base_url="https://jsonplaceholder.typicode.com")

def test_get_posts(api_client):
    response = api_client.get("posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_post(api_client):
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.post("posts",data=data)
    assert response.status_code == 201
    assert response.json()['title'] == "foo"

def test_update_data(api_client):
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_client.put("posts/1",data=data)
    assert response.status_code == 200
    assert response.json()["title"] == "foo"
