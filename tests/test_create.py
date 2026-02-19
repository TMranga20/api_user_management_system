from utils.api_client import APIClient
from utils.test_data import create_user_data

client = APIClient()

def test_create_user():
    response = client.create_user(
        create_user_data["name"],
        create_user_data["job"]
    )

    assert response.status_code == 201
    assert response.json()["name"] == create_user_data["name"]

