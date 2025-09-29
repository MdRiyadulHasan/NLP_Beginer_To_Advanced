from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus
docs = [
    "I love NLP",
    "I love machine learning",
    "NLP loves machine learning"
]

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer()

# Fit and transform the corpus
tfidf_matrix = tfidf.fit_transform(docs)

# Vocabulary
print("Vocabulary:", tfidf.get_feature_names_out())

# TF-IDF matrix
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())



