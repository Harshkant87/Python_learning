import folium
map = folium.Map(location = [25.555330, 85.089368], tiles="cartodb positron")

fg = folium.FeatureGroup(name = "My map")
fg.add_child(folium.Marker(location = [25.6, 85.1], popup = "Hi I am here!",  icon = folium.Icon(color = "red")))

map.add_child(fg)
map.save("Map1.html")
