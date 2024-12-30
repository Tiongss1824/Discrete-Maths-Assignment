import csv
from prettytable import PrettyTable

# Step 1: Create a CSV file
csv_file = "Anime_songs.csv"
data = [
    ["Anime","Song Name", "YouTube URL"],
    ["Beastars","Into the world", "https://youtu.be/gOTNI5smH2E?si=tx-a6c-nbpnpxnuQ"],
    ["JOJO'S BIZARRE ADVENTURE -Golden Wind", "il vento d'oro", "https://youtu.be/U0TXIXTzJEY?si=_hhSRvvkQbbl-v9v"],
    ["DAN DA DAN","Otonoke", "https://youtu.be/a4na2opArGY?si=HV4IUYiz6Eu3rEAA"],
    ["CHAINSAW MAN", "KICK BACK", "https://youtu.be/dFlDRhvM4L0?si=oI4CvbboaL7LCe4g"],
    ["呪術廻戦", "青のすみか", "https://youtu.be/gcgKUcJKxIs?si=s3rQqBTTBV6joPB9"],
    ["Cyberpunk: Edgerunners", "I Really Want to Stay At Your House", "https://youtu.be/KvMY1uzSC1E?si=AHGC6cSVzrpIBS0z"],
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
