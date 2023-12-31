import folium
import pandas

map = folium.Map(location = [25.555330, 85.089368], tiles="cartodb positron")
fg = folium.FeatureGroup(name = "My map")
data = pandas.read_csv("national_parks.txt")
latitudes = list(data['Latitude'])
longitudes = list(data['Longitude'])
places = list(data['Place'])
names = list(data['Name'])

def color_producer(longitude):
    if longitude < 80.0:
        return 'red'
    else:
        return 'green'

for i in range(len(names)):
    fg.add_child(folium.Marker(location = [latitudes[i], longitudes[i]], popup = names[i] + "," + places[i] ,  icon = folium.Icon(color = color_producer(longitudes[i])), fill_opacity = 0.5))

fg.add_child(folium.GeoJson(data = ( open("world-countries.json", 'r', encoding = 'utf-8-sig').read())))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("national_parks_map.html")
