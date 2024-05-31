import requests
import json

url = "http://localhost:8002/user/creatTask"
data = {
    "accessToken": "870cb511",
    "collar_id": "12",
    "task": "Help this poor dog"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())