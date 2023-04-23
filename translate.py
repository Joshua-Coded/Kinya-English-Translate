import pandas as pd

# Load the data from a CSV file
df = pd.read_csv('preprocessed_english_kinyarwanda_dictionary.csv')

# Check if the 'Kinyarwanda' column exists
if 'Kinyarwanda' not in df.columns:
    print("Error: Kinyarwanda column not found")
    # Do something else, like exiting the program or loading default values
else:
    # Do something with the 'Kinyarwanda' column
    kinyarwanda_data = df['Kinyarwanda']
    # ...