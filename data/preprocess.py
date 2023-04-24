import pandas as pd
import re

# Read the data from the text files
kinyarwanda_sentences = []
english_sentences = []

for i in range(1, 7):
    with open(f'dev/dev-kin.txt', 'r') as f:
        kinyarwanda_text = f.read()
    with open(f'dev/dev-en.txt', 'r') as f:
        english_text = f.read()

    # Split the text into sentences
    kinyarwanda_sentences_i = re.split(r'[.!?]+', kinyarwanda_text)
    english_sentences_i = re.split(r'[.!?]+', english_text)

    # Remove any leading or trailing spaces from the sentences
    kinyarwanda_sentences_i = [s.strip() for s in kinyarwanda_sentences_i]
    english_sentences_i = [s.strip() for s in english_sentences_i]

    # Append the sentences to the lists
    kinyarwanda_sentences += kinyarwanda_sentences_i
    english_sentences += english_sentences_i

# Make sure the two lists have the same length
min_len = min(len(kinyarwanda_sentences), len(english_sentences))
kinyarwanda_sentences = kinyarwanda_sentences[:min_len]
english_sentences = english_sentences[:min_len]

# Create a DataFrame with the sentences
df = pd.DataFrame({
    'Kinyarwanda': kinyarwanda_sentences,
    'English': english_sentences
})

# Preprocess the data
df['Kinyarwanda'] = df['Kinyarwanda'].apply(lambda x: x.lower())
df['English'] = df['English'].apply(lambda x: x.lower())
df['Kinyarwanda'] = df['Kinyarwanda'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df['English'] = df['English'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

# Save the preprocessed data to a CSV file
df.to_csv('preprocessed_data.csv', index=False)
