import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the preprocessed data into a DataFrame
df = pd.read_csv('preprocessed_english_kinyarwanda_dictionary.csv')

# Check if the 'Kinyarwanda' column is present in the DataFrame
if 'Kinyarwanda' in df.columns:
    # Convert the 'Kinyarwanda' column to lowercase
    df['Kinyarwanda'] = df['Kinyarwanda'].str.lower()

    # Split the data into training and testing sets
    train_df = df.sample(frac=0.8, random_state=42)
    test_df = df.drop(train_df.index)

    # Create a CountVectorizer object and fit it to the training data
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(train_df['English'])
    y_train = train_df['Kinyarwanda']

    # Train a Multinomial Naive Bayes classifier
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # Evaluate the model on the testing set
    X_test = vectorizer.transform(test_df['English'])
    y_test = test_df['Kinyarwanda']
    score = clf.score(X_test, y_test)
    print(f"Accuracy: {score:.2f}")
else:
    print("Error: Kinyarwanda column not found")
