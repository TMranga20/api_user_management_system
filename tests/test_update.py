from utils.api_client import APIClient
from utils.test_data import update_user_data

client = APIClient()

def test_update_user():
    response = client.update_user(
        2,
        update_user_data["name"],
        update_user_data["job"]
    )

    assert response.status_code == 200
    assert response.json()["name"] == update_user_data["name"]
