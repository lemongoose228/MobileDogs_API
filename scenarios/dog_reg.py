import requests
import json

url = "http://localhost:8002/dogs/registr"
data = {
    "name": "Oslik",
    "collar_id": "12"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())