import math

def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_latitude = math.radians((a_lat + b_lat) / 2.0)
    lat_lon_factor = math.cos(radians_latitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance

if __name__ == "__main__":
    # Ввод адресов пользователя
    home_address = input("Введите адрес вашего дома: ")
    university_address = input("Введите адрес университета: ")

    # Преобразование адресов в координаты с использованием API геокодирования
    # Здесь вам понадобится API ключ от сервиса геокодирования, например, от Яндекс.Карт или Google Maps
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

    home_coords = get_coordinates(home_address, YANDEX_API_KEY)
    university_coords = get_coordinates(university_address, YANDEX_API_KEY)

    if home_coords and university_coords:
        distance = lonlat_distance(home_coords, university_coords)
        print(f"Расстояние от дома до университета: {distance:.2f} метров")
    else:
        print("Не удалось определить координаты для одного из адресов.")
