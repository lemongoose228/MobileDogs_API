import pytest
#import src.devices.router as router
#import src.users.router as router1
from fastapi.testclient import TestClient
import random
from src.database import BaseDBModel, engine

from src.main import app

client = TestClient(app)

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

async def test_dogs_registration():
    name = generate_random_string(7)
    collar_id = random.randint(0, 200)

    response = client.post("/dogs/register", json={
            "name": name,
            "collar_id": collar_id,
    })

    while (response.status_code!=200):
        name = generate_random_string(7)
        collar_id = random.randint(0, 200)

        response = client.post("/dogs/register", json={
            "name": name,
            "collar_id": collar_id,
        })

    return response.json()["collar_token"]
