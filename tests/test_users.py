import random
import string

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_users_registration():
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(9))

    response = client.post("/user/registr", json={
            "login": name,
            "password": password,
    })

    while (response.status_code!=200):
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        password = ''.join(random.choice(string.ascii_lowercase) for i in range(9))

        response = client.post("/user/registr", json={
            "login": name,
            "password": password,
        })

    return response.json()["accessToken"]
