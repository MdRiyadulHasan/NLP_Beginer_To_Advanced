import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# # Download resources (first time only)
# nltk.download('punkt')
# nltk.download('stopwords')

# Example dataset (list of sentences/documents)
dataset = [
    "This is the first document.",
    "Natural Language Processing is amazing for text analysis!",
    "Stop words should be removed before training a model.",
    "Sometimes stop words are important in sentiment analysis."
]

# English stop words
stop_words = set(stopwords.words('english'))

# Function to clean text
def remove_stopwords(text):
    words = word_tokenize(text)
    filtered = [w for w in words if w.lower() not in stop_words]
    return " ".join(filtered)

# Apply to the whole dataset
cleaned_dataset = [remove_stopwords(doc) for doc in dataset]

# Show results
print("=== Before & After Stopwords Removal ===\n")
for original, cleaned in zip(dataset, cleaned_dataset):
    print(f"Original : {original}")
    print(f"Cleaned  : {cleaned}")
    print("-" * 50)
