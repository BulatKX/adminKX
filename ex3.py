import requests
import os


def get_satellite_image(lat, lon, api_key, zoom=15, size="600x400", map_type="satellite"):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"

    params = {
        "center": f"{lat},{lon}",
        "zoom": zoom,
        "size": size,
        "maptype": map_type,
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Сохранение изображения в файл
        with open("satellite_image.png", "wb") as file:
            file.write(response.content)
        print("Изображение успешно сохранено в 'satellite_image.png'")
    else:
        print(f"Ошибка при получении изображения: {response.status_code}")


# Пример использования
api_key = "ВАШ_API_КЛЮЧ"
latitude = 55.755826
longitude = 37.6173

get_satellite_image(latitude, longitude, api_key)
