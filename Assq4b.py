import requests
import csv
import os

# Define the CSV file name
csv_file = 'data_gov_my_datasets.csv'

# Read data from CSV file
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Function to download a file from a URL
def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {filename} from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Download each file from the provided URLs
for entry in data:
    dataset_name = entry["dataset"].replace(" ", "_").lower()
    # Get file extension from URL, or default to 'txt' if not found
    file_extension = os.path.splitext(entry["url"])[1][1:]  # Extract extension after the dot
    if not file_extension:
        file_extension = "txt"  # Default extension if none found
    filename = f"{dataset_name}.{file_extension}"
    download_file(entry["url"], filename)

print("All files have been processed.")