import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re

labels = ["positive", "positive", "neutral", "negative"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

docs = [
    "The movie was amazing, I loved it!",
    "I am loving this film, it is fantastic!",
    "He studies the plot carefully but studying is boring.",
    "This was the worst movie, I hated it."
]


def preprocess(text, method="stem"):
    # lowercase + remove non-letters
    text = re.sub(r"[^a-zA-Z]", " ", text.lower())
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]
    
    if method == "stem":
        return [stemmer.stem(w) for w in tokens]
    else:
        return [lemmatizer.lemmatize(w, pos="v") for w in tokens]
    
for doc in docs:
    print("Original:", doc)
    print("Stemming:", preprocess(doc, "stem"))
    print("Lemmatization:", preprocess(doc, "lemma"))
    print()