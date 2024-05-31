#import src.devices.router as router
#import src.users.router as router1
from fastapi.testclient import TestClient
import random
import string
#from src.database import BaseDBModel, engine

#import src.database

from main import app

client = TestClient(app)

async def test_dogs_registration():
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
    collar_id = str(random.randint(0, 200))

    response = client.post("/dogs/register", json={
            "name": name,
            "collar_id": collar_id,
    })

    while (response.status_code!=200):
        name = rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        collar_id = random.randint(0, 200)

        response = client.post("/dogs/register", json={
            "name": name,
            "collar_id": collar_id,
        })

    return response.json()["collar_token"]
