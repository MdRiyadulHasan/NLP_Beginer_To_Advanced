import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords (first time only)
nltk.download('punkt')
nltk.download('stopwords')

text = "This is an example showing how to remove stop words from a sentence."

# Tokenize
words = word_tokenize(text)

# Get English stop words
stop_words = set(stopwords.words('english'))

# Filter words
filtered = [w for w in words if w.lower() not in stop_words]

print("Original:", words)
print("Without Stopwords:", filtered)
