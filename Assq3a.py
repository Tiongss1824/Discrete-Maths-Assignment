import folium

# Coordinates for Malaysia's center (Kuala Lumpur)
latitude = 4.2105
longitude = 101.9758

# Create a map centered on Malaysia
map_malaysia = folium.Map(location=[latitude, longitude], zoom_start=6)

# Save the map to an HTML file
map_malaysia.save("malaysia_map.html")

print("Map of Malaysia has been created and saved as 'malaysia_map.html'.")
