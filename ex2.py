import folium
from geopy.distance import geodesic

# Список координат (например, путь через Москву)
points = [
    (55.755826, 37.6173),   # Красная площадь
    (55.751244, 37.618423), # Кремль
    (55.758564, 37.617739), # Большой театр
    (55.764381, 37.622504), # Лубянка
    (55.771403, 37.630292), # Сухаревская площадь
    (55.775978, 37.641041)  # Сретенский бульвар
]

# Вычисление длины пути
total_distance = 0
for i in range(len(points) - 1):
    total_distance += geodesic(points[i], points[i+1]).kilometers

# Найдем среднюю точку
middle_index = len(points) // 2
middle_point = points[middle_index]

# Создание карты
map_moscow = folium.Map(location=points[0], zoom_start=14)

# Добавление пути на карту
folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(map_moscow)

# Добавление маркеров для каждой точки
for point in points:
    folium.Marker(location=point).add_to(map_moscow)

# Добавление маркера для средней точки
folium.Marker(location=middle_point, popup="Средняя точка", icon=folium.Icon(color='red')).add_to(map_moscow)

# Сохранение карты в HTML файл
map_moscow.save("moscow_path_map.html")

# Вывод общей длины пути
print(f"Общая длина пути: {total_distance:.2f} км")