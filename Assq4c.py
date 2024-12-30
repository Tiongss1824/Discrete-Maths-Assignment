import pandas as pd
import os

# Load the content of the text file
file_name = 'worker_salaries.txt'
df = pd.read_csv(file_name)

# Define the CSV file name
csv_file_name = 'worker_salaries.csv'

# Save the dataframe to a CSV file
df.to_csv(csv_file_name, index=False)

# Check if the file exists
if os.path.exists(file_name):
    # Delete the file
    os.remove(file_name)

print(f"The content of the file '{file_name}' has been successfully translated to '{csv_file_name}'.")