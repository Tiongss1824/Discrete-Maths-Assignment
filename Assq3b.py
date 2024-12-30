import folium
import pandas as pd

# Data with Penang Hill, KLCC Park, and A Famosa
data = {
    'name': ['Penang Hill', 'KLCC Park', 'A Famosa'],
    'description': ['Offers stunning views of the city and surrounding jungle', 'Large urban park with fountains and sculptures', 'Historic Portuguese fortress with great views'],
    'latitude': [5.4321, 3.1578, 2.1923],
    'longitude': [100.2763, 101.7115, 102.2491]
}

df = pd.DataFrame(data)

# Create a map centered around Malaysia
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Add markers for the tourist attractions
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} - {row['description']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Save the map to an HTML file
m.save('malaysia_tourist_attractions.html')
