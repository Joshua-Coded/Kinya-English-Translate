import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load pre-trained model
model = load_model('model.h5')

# Load test dataset
test_df = pd.read_csv('preprocessed_english_kinyarwanda_dictionary.csv')

# Remove 'Kinyarwanda' column
if 'Kinyarwanda' in test_df.columns:
    test_df = test_df.drop(columns=['Kinyarwanda'])

# Convert text to sequence
test_sequences = [text.split() for text in test_df['English']]
test_sequences = [[word_index.get(word.lower(), 1) for word in seq] for seq in test_sequences]
test_sequences = pad_sequences(test_sequences, padding='post')

# Make prediction
predictions = model.predict(test_sequences)

# Convert prediction to text
y_pred = [' '.join([reverse_word_index.get(idx, '<UNK>') for idx in seq]) for seq in predictions.argmax(axis=1)]

# Save predictions to CSV file
test_df['Kinyarwanda'] = y_pred
test_df.to_csv('preprocessed_english_kinyarwanda_dictionary.csv', index=False)