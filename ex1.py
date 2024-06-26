import folium

# Координаты стадионов
stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540"
}

# Создание карты с центром в Москве
map_moscow = folium.Map(location=[55.751244, 37.618423], zoom_start=11)

# Добавление меток для каждого стадиона
for stadium, coord in stadiums_location.items():
    lat, lon = map(float, coord.split(','))
    folium.Marker(
        location=[lon, lat],
        popup=stadium,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map_moscow)

# Сохранение карты в HTML файл
map_moscow.save("moscow_stadiums_map.html")

# Отображение карты в Jupyter Notebook (если используется)
map_moscow