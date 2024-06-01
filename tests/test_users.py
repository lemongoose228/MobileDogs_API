import random
import string

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_users_registration():
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(9))

    response = client.post("/user/registr", json={
            "login": name,
            "password": password,
    })

    return response.json()["accessToken"]

def test_users_login():
    login = "meitoav"
    password = "szkogjtxs"
    token = "1b3136dc"

    response = client.post("/user/login", json={
            "login": login,
            "password": password,
            "accessToken": token,
    })

    assert response.status_code == 200
    #assert response.json()['message'] == 'Вы успешно вошли в аккаунт'

def test_users_createTask():
    login = "meitoav"
    password = "szkogjtxs"
    token = "1b3136dc"

    response = client.post("/user/login", json={
            "login": login,
            "password": password,
            "accessToken": token,
    })

    assert response.status_code == 200

def test_users_subscribe():
    login = "meitoav"
    collar_id = "6"
    token = "1b3136dc"

    response = client.post("/user/subscribe", json={
            "user_login": login,
            "password": collar_id,
            "accessToken": token,
    })

    assert response.status_code == 422

def test_users_unsubscribe():
    login = "meitoav"
    collar_id = "6"
    token = "1b3136dc"

    response = client.post("/user/unsubscribe", json={
        "accessToken": token,
        "collar_id": collar_id,
        "task": "Help dogich",
    })

    assert response.status_code == 422
