from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


data = [
    ("Free entry in 2 a weekly competition! Text WIN to 12345", "spam"),
    ("Hey, are we still meeting today?", "ham"),
    ("Congratulations! You won a lottery. Call now!", "spam"),
    ("Don't forget to bring the documents.", "ham"),
    ("URGENT! Claim your free gift card today!", "spam"),
    ("Can you send me the report by tonight?", "ham")
]

# Split messages and labels
texts, labels = zip(*data)


# Initialize TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')  # remove common words

# Fit and transform the text
X = tfidf.fit_transform(texts)

# Show feature names (vocabulary)
print("Vocabulary:", tfidf.get_feature_names_out())

# Show TF-IDF matrix
print("TF-IDF Matrix:\n", X.toarray())



X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.33, random_state=42
)


# Train Multinomial Naive Bayes
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Predict on test set
y_pred = nb.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

new_messages = [
    "Win a free iPhone now by clicking here",
    "Are we having lunch tomorrow?"
]

# Transform using same TF-IDF vectorizer
X_new = tfidf.transform(new_messages)
predictions = nb.predict(X_new)

for msg, label in zip(new_messages, predictions):
    print(f"Message: {msg}\nPredicted label: {label}\n")
