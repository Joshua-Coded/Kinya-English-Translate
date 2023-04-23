import pandas as pd
import joblib

# Load the preprocessed dataset
test_df = pd.read_csv('preprocessed_english_kinyarwanda_dictionary.csv')

# Remove the 'Kinyarwanda' column
test_df = test_df.drop(columns=['Kinyarwanda'])

# Load the trained model
clf = joblib.load('text_classification_model.joblib')

# Split the data into input features and target labels
X_train = test_df['English']
y_train = test_df['Part_of_Speech']

# Make predictions on the test data
y_pred = clf.predict(X_train)

# Print the predicted values
print(y_pred)