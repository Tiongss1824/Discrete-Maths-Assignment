import csv
from prettytable import PrettyTable

# Step 1: Create a CSV file
csv_file = "Anime_songs.csv"
data = [
    ["Anime","Song Name", "YouTube URL"],
    ["Attack on Titan","Shinzou wo Sasageyo", "https://youtu.be/CID-sYQNCew?si=RtkliiGMVXF5daNs"],
    ["Violet Evergarden", "Sincerely", "https://youtu.be/rh-xfHTJp6M?si=sPpzAWDzzJishB-x"], # this song is too good!
    ["葬送のフリーレン","勇者", "https://youtu.be/OIBODIPC_8Y?si=bxSJ6zHFMe-zQgbl"],
]

# Write data to the CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Step 2: Read the CSV file and display it as a table
table = PrettyTable()

with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:  # First row contains headers
            table.field_names = row
        else:
            table.add_row(row)

# Display the table
print(table)
