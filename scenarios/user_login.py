import requests
import json

url = "http://localhost:8002/user/login"
data = {
    "login": "user30301",
    "password": "superpassword",
    "accessToken": "870cb511"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())