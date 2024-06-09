import requests

def get_coordinates(address, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return (location['lat'], location['lng'])
        else:
            print(f"Не удалось найти координаты для адреса {address}")
            return None
    else:
        print(f"Ошибка при запросе координат: {response.status_code}")
        return None

def find_nearest_pharmacy(lat, lon, api_key):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": 5000,  # Радиус поиска в метрах
        "type": "pharmacy",
        "key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            nearest_pharmacy = data['results'][0]
            name = nearest_pharmacy['name']
            address = nearest_pharmacy['vicinity']
            return (name, address)
        else:
            print("Аптеки не найдены в указанном радиусе.")
            return None
    else:
        print(f"Ошибка при запросе данных о местах: {response.status_code}")
        return None

if __name__ == "__main__":
    api_key = "ВАШ_API_КЛЮЧ"
    address = input("Введите адрес: ")

    coordinates = get_coordinates(address, api_key)
    if coordinates:
        lat, lon = coordinates
        pharmacy = find_nearest_pharmacy(lat, lon, api_key)
        if pharmacy:
            name, address = pharmacy
            print(f"Ближайшая аптека: {name}, Адрес: {address}")
        else:
            print("Не удалось найти ближайшую аптеку.")
    else:
        print("Не удалось определить координаты для указанного адреса.")
