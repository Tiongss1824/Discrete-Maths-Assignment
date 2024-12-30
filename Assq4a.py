import csv

# Data from data.gov.my
data = [
    {
        "source": "Data.gov.my",
        "dataset": "Worker Salaries",
        "url": "https://archive.data.gov.my/data/en_US/datastore/dump/4ce4ccf6-f2a2-4a40-9bc0-9a44e0400e4a"
    },
    {
        "source": "github.com",
        "dataset": "House Prices",
        "url": "https://raw.githubusercontent.com/ShraqueOatMeal/Malaysia-House-Price-Prediction/a4fe09d3deec98249c5a2a0004d3f82fc152dd07/mas_housing.csv"
    },
]

# Define the CSV file name
csv_file = 'data_gov_my_datasets.csv'

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["source", "dataset", "url"])
    writer.writeheader()
    for entry in data:
        writer.writerow(entry)

print(f"CSV file '{csv_file}' has been created with the data from data.gov.my.")