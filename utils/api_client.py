import os
import requests


class APIClient:
    BASE_URL = "https://reqres.in/api"

    def __init__(self):
        api_key = os.getenv("REQRES_API_KEY")

        if not api_key:
            raise ValueError(
                "API key not found. Set REQRES_API_KEY environment variable."
            )

        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def _request(self, method, endpoint, payload=None):
        url = f"{self.BASE_URL}{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            headers=self.headers
        )

        print("\nREQUEST:")
        print("URL:", url)
        print("METHOD:", method)
        print("HEADERS:", self.headers)
        print("PAYLOAD:", payload)

        print("\nRESPONSE:")
        print("STATUS CODE:", response.status_code)
        print("BODY:", response.text)

        return response

    # CREATE USER
    def create_user(self, name, job):
        payload = {
            "name": name,
            "job": job
        }
        return self._request("POST", "/users", payload)

    # GET USER
    def get_user(self, user_id):
        return self._request("GET", f"/users/{user_id}")

    # UPDATE USER
    def update_user(self, user_id, name, job):
        payload = {
            "name": name,
            "job": job
        }
        return self._request("PUT", f"/users/{user_id}", payload)

    # DELETE USER
    def delete_user(self, user_id):
        return self._request("DELETE", f"/users/{user_id}")
