from sklearn.feature_extraction.text import CountVectorizer

# Our small corpus
docs = [
    "I love NLP",
    "I love machine learning",
    "NLP loves machine learning"
]

# Initialize Bag-of-Words vectorizer
vectorizer = CountVectorizer()

# Fit to the corpus and transform
bow_matrix = vectorizer.fit_transform(docs)

# Show vocabulary
print("Vocabulary:", vectorizer.get_feature_names_out())

# Show BoW matrix
print("BoW Matrix:\n", bow_matrix.toarray())
