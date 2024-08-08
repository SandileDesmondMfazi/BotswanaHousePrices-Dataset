import pandas as pd
import os

# Load datasets
property24 = pd.read_csv('data/New_Property24.csv')
remax = pd.read_csv('data/New_ReMax.csv')
seeff = pd.read_csv('data/New_Seeff.csv')

# Combine datasets
combined_df = pd.concat([property24, remax, seeff], ignore_index=True)

# Rename columns
combined_df.columns = ['Id','Property_Title', 'Location', 'Description', 'Link', 'Bedrooms', 'Bathrooms', 'Parking_Spaces', 'Erf_Size', 'Agency', 'Price']

# Get the absolute path to the data directory
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

# Save the combined dataset
combined_df.to_csv(os.path.join(data_dir, 'Botswana_Property_Prices.csv'), index=False, encoding='utf-8')

# Print the first few rows to verify
print(combined_df.head())