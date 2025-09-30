import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
text = """
Apple is looking to buy a startup in the UK for $1 billion. 
Meanwhile, Microsoft announced a new product launch in India next week.
"""
# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words and token.isalpha()]

print("Filtered Tokens (NLTK):", filtered_tokens)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Process the original text with spaCy
doc = nlp(text)

# Part-of-Speech tagging
print("\nPOS Tagging:")
for token in doc:
    print(token.text, token.pos_, token.dep_)

# Named Entity Recognition
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)
