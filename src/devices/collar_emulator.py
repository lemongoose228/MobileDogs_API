import requests
import time
import random

BASE_URL = "http://localhost:8002" # Адрес вашего FastAPI приложения

def generate_coordinates():
    # Генерируем случайные координаты широты и долготы
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)

    return latitude, longitude

while True:
    # Генерируем координаты
    latitude, longitude = generate_coordinates()

    # Отправляем POST запрос на сервер
    data = {
        "id": 1, # ID ошейника
        "latitude": latitude,
        "longitude": longitude
    }

    response = requests.post(f"{BASE_URL}/dogs/getDogsGeoPos", json=data)

    if response.status_code == 200:
        print("Данные успешно отправлены")
    else:
        print(f"Произошла ошибка: {response.text}")
