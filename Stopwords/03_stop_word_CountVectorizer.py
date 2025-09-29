from sklearn.feature_extraction.text import CountVectorizer

text = ["This is an example showing how to remove stop words with sklearn"]

# Vectorizer with built-in English stop words
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text)

print("Vocabulary:", vectorizer.get_feature_names_out())