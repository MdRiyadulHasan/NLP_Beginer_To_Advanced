import nltk

# Ensure required tokenizers are available
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.tokenize import word_tokenize

text = "Hello, I am learning NLP with Python."
words = word_tokenize(text)
print(words)
