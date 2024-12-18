import pandas as pd
import os

# Read the CSV data
df = pd.read_csv('Data/crimeRate.csv')

# Sort the data based on crimeRate in ascending order
sorted_df = df.sort_values(by='crimeRate', ascending=True)

# Add a Rank column
sorted_df['Rank'] = range(1, len(sorted_df) + 1)

# Reorder columns to have Rank as the first column
sorted_df = sorted_df[['Rank', 'State/UT', 'crimeRate']]

# Create 'processedData' folder if it doesn't exist
output_file = 'Data/processedData/crimeData.csv'
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Save the sorted and ranked data to a new CSV file
sorted_df.to_csv(output_file, index=False)

print(f"Sorted and ranked crime data has been saved to {output_file}")

# Display the first few rows of the sorted data
print(sorted_df.head())