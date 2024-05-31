import requests
import json

url = "http://localhost:8002/user/takeTask"
data = {
    "accessToken": "a5792cd2",
    "task_id": 1
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())