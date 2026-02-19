from utils.api_client import APIClient

client = APIClient()

def test_delete_user():
    response = client.delete_user(2)

    assert response.status_code == 204
