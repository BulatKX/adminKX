import requests
import sys
# Запустите скрипт script.py из командной строки, передав адрес в качестве аргумента
YANDEX_API_KEY = "89bfcbad-6762-4716-b21c-44efce35631d"


def get_coordinates(address, api_key):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "format": "json",
        "apikey": api_key
    }
    response = requests.get(geocode_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['response']['GeoObjectCollection']['featureMember']:
            point = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lon, lat = point.split()
            return float(lat), float(lon)
        else:
            print(f"Не удалось найти координаты для адреса {address}")
            return None
    else:
        print(f"Ошибка при запросе координат: {response.status_code}")
        return None


def get_district(lat, lon, api_key):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": f"{lon},{lat}",
        "kind": "district",
        "format": "json",
        "apikey": api_key
    }
    response = requests.get(geocode_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['response']['GeoObjectCollection']['featureMember']:
            district = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
            return district
        else:
            print(f"Не удалось определить район для координат {lat}, {lon}")
            return None
    else:
        print(f"Ошибка при запросе данных о районе: {response.status_code}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python script.py 'адрес'")
        sys.exit(1)

    address = sys.argv[1]

    coordinates = get_coordinates(address, YANDEX_API_KEY)
    if coordinates:
        lat, lon = coordinates
        district = get_district(lat, lon, YANDEX_API_KEY)
        if district:
            print(f"Адрес: {address}")
            print(f"Координаты: {lat}, {lon}")
            print(f"Район: {district}")
        else:
            print("Не удалось определить район.")
    else:
        print("Не удалось получить координаты.")
