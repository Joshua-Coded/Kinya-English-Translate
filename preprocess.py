import pandas as pd

# Load the scraped data into a DataFrame
df = pd.read_csv('english-kinyarwanda-dictionary.csv')

# Rename the 'DICTIONARY' column to 'English'
df = df.rename(columns={'DICTIONARY': 'English'})

# Convert the 'English' column to lowercase
df['English'] = df['English'].str.lower()

# Drop any rows with missing values
df = df.dropna()

# Save the preprocessed data to a new CSV file
df.to_csv('preprocessed_english_kinyarwanda_dictionary.csv', index=False)