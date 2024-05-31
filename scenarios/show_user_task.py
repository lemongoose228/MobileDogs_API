import requests
import json

url = "http://localhost:8002/user/showUserTasks"
data = {
    "accessToken": "870cb511"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())