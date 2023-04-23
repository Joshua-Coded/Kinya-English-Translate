import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load scraped dataset into a pandas DataFrame
df = pd.read_csv('kinyarwanda_english.csv ')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove irrelevant or incomplete data
df = df[df['word'].apply(lambda x: bool(re.match('^[a-zA-Z\s-]+$', x))) & df['definition'].notna()]

# Tokenization
nltk.download('punkt')
df['tokens'] = df['definition'].apply(lambda x: nltk.word_tokenize(x.lower()))

# Stopword removal
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])

# Lemmatization
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
df['lemmas'] = df['tokens'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# Encoding (if applicable)
# df['language_encoded'] = pd.factorize(df['language'])[0]

# Save preprocessed dataset to a new CSV file
df.to_csv('preprocessed_data.csv', index=False)
