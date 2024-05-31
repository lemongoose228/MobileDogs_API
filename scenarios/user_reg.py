import requests
import json

url = "http://localhost:8002/user/registr"
data = {
    "login": "user30301",
    "password": "superpassword"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
