import json
import folium

with open('data/kisar coordinates.geojson') as json_data:
    data = json.load(json_data)
    features = data['features'][0]

coordinates = features['geometry']['coordinates']

# somehow the latitude and longitude are swapped around
kisar_map = folium.Map(location=coordinates[::-1])
folium.GeoJson(open('data/kisar way.geojson'),
               name='way').add_to(kisar_map)
folium.GeoJson(open('data/peaks in kisar.geojson'),
               name='peak').add_to(kisar_map)
folium.GeoJson(open('data/pier in kisar.geojson'),
               name='pier').add_to(kisar_map)
folium.GeoJson(open('data/airport in kisar.geojson'),
               name='airport').add_to(kisar_map)
folium.GeoJson(open('data/water in kisar.geojson'),
               name='water').add_to(kisar_map)
folium.LayerControl().add_to(kisar_map)
kisar_map.save('index.html')
