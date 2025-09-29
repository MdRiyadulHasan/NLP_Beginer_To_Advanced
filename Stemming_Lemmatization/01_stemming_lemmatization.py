import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary resources (run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["running", "runner", "studies", "studying", "better"]

print("Stemming:")
for w in words:
    print(w, "→", stemmer.stem(w))

print("\nLemmatization:")
for w in words:
    print(w, "→", lemmatizer.lemmatize(w, pos='v'))  # 'v' means verb
