import folium
import pandas as pd

# Data with Penang Hill, KLCC Park, and A Famosa
data = {
    'name': ['Penang Hill', 'KLCC Park', 'A Famosa'],
    'description': ['Offers stunning views of the city and surrounding jungle', 'Large urban park with fountains and sculptures', 'Historic Portuguese fortress with great views'],
    'latitude': [5.4321, 3.1578, 2.1923],
    'longitude': [100.2763, 101.7115, 102.2491],
    'category': ['Natural Wonder', 'Urban Park', 'Historical Site']
}

df = pd.DataFrame(data)

# Create a map centered around Malaysia
m = folium.Map(location=[4.2105, 101.9758], zoom_start=6)

# Define colors for each category
color_dict = {
    'Natural Wonder': 'green',
    'Urban Park': 'blue',
    'Historical Site': 'red'
}

# Add markers to different feature groups based on categories
natural_wonders = folium.FeatureGroup(name='Natural Wonders')
urban_parks = folium.FeatureGroup(name='Urban Parks')
historical_sites = folium.FeatureGroup(name='Historical Sites')

for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['name']} - {row['description']}",
        icon=folium.Icon(color=color_dict[row['category']], icon='info-sign')
    ).add_to(eval(f"{row['category'].lower().replace(' ', '_')}s"))

natural_wonders.add_to(m)
urban_parks.add_to(m)
historical_sites.add_to(m)

# Add layer control to toggle different types of attractions
folium.LayerControl().add_to(m)

# Save the map to an HTML file
m.save('malaysia_tourist_attractions_v2.html')
