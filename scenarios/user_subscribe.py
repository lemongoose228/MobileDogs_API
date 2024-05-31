import requests
import json

url = "http://localhost:8002/user/subscribe"
data = {
    "user_login": "user30301",
    "collar_id": "12",
    "accessToken": "870cb511"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())