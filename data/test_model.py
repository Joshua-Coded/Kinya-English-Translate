import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import MarianMTModel, MarianTokenizer

# Load the preprocessed data
df = pd.read_csv('preprocessed_data.csv')

# Split the data into training and validation sets
train_df, val_df = train_test_split(df, test_size=0.1, random_state=42)

# Load the MarianMTModel and MarianTokenizer
model_name = 'Helsinki-NLP/opus-mt-rw-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Define the function for translating text
def translate_text(text, max_length=512):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=max_length)

    # Generate the translation
    outputs = model.generate(**inputs)

    # Decode the translation
    translated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return translated_text[0]

# Translate a sample sentence
sentence = 'ndabona iteka rya nyuma'
translation = translate_text(sentence)
print(f'Kinyarwanda: {sentence}')
print(f'English: {translation}')

# Evaluate the model on the validation set
val_df['Translated'] = val_df['Kinyarwanda'].apply(translate_text)
accuracy = (val_df['English'] == val_df['Translated']).mean()
print(f'Validation accuracy: {accuracy:.4f}')
