import sys
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_locator")
    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            print(f"Не удалось найти координаты для города {city_name}")
            return None
    except GeocoderTimedOut:
        print(f"Ошибка таймаута при получении координат для города {city_name}")
        return None


def find_southernmost_city(cities):
    southernmost_city = None
    southernmost_latitude = float('inf')

    for city in cities:
        coordinates = get_coordinates(city)
        if coordinates:
            latitude, _ = coordinates
            if latitude < southernmost_latitude:
                southernmost_latitude = latitude
                southernmost_city = city

    return southernmost_city


if __name__ == "__main__":
    input_cities = input("Введите список городов через запятую: ")
    cities = [city.strip() for city in input_cities.split(",")]

    if not cities:
        print("Список городов пуст.")
        sys.exit(1)

    southernmost_city = find_southernmost_city(cities)

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить самый южный город.")
