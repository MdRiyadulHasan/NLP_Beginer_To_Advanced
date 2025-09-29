from sklearn.feature_extraction.text import CountVectorizer

text = ["This is an example showing how to remove stop words with sklearn"]

# Vectorizer with built-in English stop words
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text)

print("Vocabulary:", vectorizer.get_feature_names_out())


# another example


corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(corpus)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("Vectorized Matrix:\n", X.toarray())