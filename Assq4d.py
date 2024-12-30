import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io # import the io module

data_files = [
    'worker_salaries.csv',
    'house_prices.csv', 
]

dataframes = {}

for file in data_files:
    try:
        if file == 'house_prices.csv':  # Apply this only to house_prices.csv
            # Read the file content as bytes
            with open(file, 'rb') as f:
                content = f.read()

            # Decode the content using 'latin1' and ignore errors
            decoded_content = content.decode('latin1', errors='ignore')

            # Read the CSV from the decoded content using io.StringIO
            # Use on_bad_lines instead of error_bad_lines
            df = pd.read_csv(io.StringIO(decoded_content), sep=',', on_bad_lines='skip')
        else:
            df = pd.read_csv(file)

        dataframes[file] = df

    except FileNotFoundError:
        print(f"file {file} not found, make sure on the correct path")

for file, df in dataframes.items():
    print(f"\n--- data collection：{file} ---")

    print("\nStatistic：")
    print(df.describe())

    for column in df.select_dtypes(include=['number']).columns:
        plt.figure()
        plt.hist(df[column], bins=10)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {column}')
        plt.show()

    numeric_columns = df.select_dtypes(include=['number']).columns
    for i in range(len(numeric_columns)):
        for j in range(i + 1, len(numeric_columns)):
            plt.figure()
            plt.scatter(df[numeric_columns[i]], df[numeric_columns[j]])
            plt.xlabel(numeric_columns[i])
            plt.ylabel(numeric_columns[j])
            plt.title(f'Relationship between {numeric_columns[i]} and {numeric_columns[j]}')
            plt.show()
    numeric_df = df.select_dtypes(include=['number'])

    plt.figure()
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()