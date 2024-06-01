from fastapi.testclient import TestClient
import random
import string
import pytest

from src.main import app

client = TestClient(app)

def test_dogs_registration():
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
    collar_id = str(random.randint(0, 200))

    response = client.post("/dogs/registr", json={
            "name": name,
            "collar_id": collar_id
    })

    return response.json()["collar_token"]

def test_dogs_registration_already_exist():
    name = "Buba"
    collar_id = "6"

    response = client.post("/dogs/registr", json={
            "name": name,
            "collar_id": collar_id,
    })

    assert response.status_code == 400
    assert response.json()['detail'] == 'Этот ошейник занят'

def test_dogs_registration_already_exist():
    name = "Buba"
    collar_id = "6"

    response = client.post("/dogs/registr", json={
            "name": name,
            "collar_id": collar_id
    })

    assert response.status_code == 400
    assert response.json()['detail'] == 'Этот ошейник занят'
