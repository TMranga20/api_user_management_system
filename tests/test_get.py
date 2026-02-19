from utils.api_client import APIClient

client = APIClient()

def test_get_user():
    response = client.get_user(2)

    print(response.status_code)
    print(response.text)


    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
