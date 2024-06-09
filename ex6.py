import requests
import random
import os
from PIL import Image
from io import BytesIO

# Константный список городов
CITIES = [
    "Москва", "Нью-Йорк", "Лондон", "Токио", "Париж",
    "Сидней", "Рио-де-Жанейро", "Каир", "Берлин", "Мадрид"
]

API_KEY = "ВАШ_API_КЛЮЧ"


def get_random_map(city, api_key):
    map_types = ['roadmap', 'satellite']
    map_type = random.choice(map_types)
    zoom = random.randint(12, 16)  # случайный уровень масштабирования
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"

    params = {
        "center": city,
        "zoom": zoom,
        "size": "600x400",
        "maptype": map_type,
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        print(f"Ошибка при запросе карты для {city}: {response.status_code}")
        return None


def create_slideshow(images):
    for i, img in enumerate(images):
        img.save(f"city_{i}.png")
    # Можно использовать любой инструмент для создания слайд-шоу, например, ffmpeg, чтобы создать видео из изображений.


if __name__ == "__main__":
    images = []
    for city in CITIES:
        img = get_random_map(city, API_KEY)
        if img:
            images.append(img)

    random.shuffle(images)
    create_slideshow(images)
    print("Слайд-шоу создано.")
